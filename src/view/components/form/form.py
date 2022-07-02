from typing import Union
from .form_components import add_input, add_select


def form_controller(type: str, **kwargs) -> Union[str, int]:
    """The form_controller function builds a form component based on a given `type`."""
    form_factories = {"input": add_input, "select": add_select}

    return form_factories[type](**kwargs)
