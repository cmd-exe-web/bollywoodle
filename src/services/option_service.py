from ..models.option import Option


class OptionService:
    @staticmethod
    def get_all_options():
        return Option.objects()

    @staticmethod
    def get_option_by_id(option_id):
        return Option.objects.get(id=option_id)

    @staticmethod
    def get_option_by_name(name):
        return Option.objects.get(name=name)

    @staticmethod
    def create_option(name):
        new_option = Option(name=name)
        new_option.save()
        return new_option

    @staticmethod
    def update_option(option_id, name):
        option = Option.objects(id=option_id).first()
        if option:
            option.name = name
            option.save()
            return option
        return None

    @staticmethod
    def delete_option(option_id):
        option = Option.objects(id=option_id).first()
        if option:
            option.delete()
            return True
        return False
