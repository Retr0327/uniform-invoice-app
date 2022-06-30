from .form_components import add_input, add_select


def create_form(type: str, **kwargs) -> str:
    form_factories = {"input": add_input, "select": add_select}

    return form_factories[type](**kwargs)
