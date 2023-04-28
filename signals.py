# При создании/обновлении Договора в ЭДО создаем/обновляем Договор в Навигаторе
# django/extedu/payment/modules/contract/models.py

class ContractOdoPayer(models.Model):
    agreement_number = models.IntegerField(
        'Contract ID from Navi',
        null=True,
        blank=True,
    )

@atomic
# Сигнал, отправляемый в Навигатор. sender=Модель
@receiver(post_save, sender=ContractOdoPayer)
# instance = our object (contract)
def post_after_save(instance: ContractOdoPayer, created: bool, **kwargs):

    contract = instance

    # setting up a client with url
    client = APIClientNavigator(url=settings.NAVIGATOR_URL)

    # preparing data (fields) for sending
    data = {
        'UF_CONTRACTNUM': contract.agreement_number,
    }

    # if the object is created and not edited
    if created:
        #getting response from Navigator
        response_data = client.get(url=UrlNavigator.URL_CONTRACT.value)
        try:
            # saving the response as json
            response_data = response_data.json()
        except JSONDecodeError:
            # raising the exception if Navigator is unavailable
            raise ApplicationLogicException('Editing is not available at the moment.')
        # creating variable for counting the total number of contracts from Navigator
        objects_count = int(response_data.get('paginator').get('objects_count'))

        # updating contract_id with the current number of objects + 1 on Navigator
        client.post(
            url=UrlNavigator.URL_CONTRACT.value,
            data=data,
        )
        # filter contracts by object's ID
        # updating contract_id field to the total number of contracts + 1
        ContractOdoPayer.objects.filter(id=contract.id).update(contract_id=objects_count + 1)

    # if the contract is updated and not created
    client.post(
        # connecting to Navigator CONTRACT_DETAIL URL
        # replacing Navigator contract's ID with contract_id
        # uploading the edited data
        url=UrlNavigator.URL_CONTRACT_DETAIL.value.replace('{id}', str(contract.contract_id)),
        data=data,
    )
