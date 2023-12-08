# taipy_test.py

import taipy as tp
from taipy import Config, Core, Gui


def build_message(name):
    """

    :param name:
    :return:
    """
    return f"Hello {name}!"


input_name_data_node_cfg = Config.configure_data_node(id="input_name")
message_data_node_cfg = Config.configure_data_node(id="message")


build_msg_task_cfg = Config.configure_task(
    "build_msg", build_message, input_name_data_node_cfg, message_data_node_cfg
)

scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])

input_name = "Grok"
message = None


def submit_scenario(state):
    """

    :param state:
    :return:
    """
    state.scenario.input_name.write(state.input_name)
    state.scenario.submit()
    state.message = scenario.message.read()


page = """
Name: <|{input_name}|input|>

<|submit|button|on_action=submit_scenario|>

Message: <|{message}|text|>
"""

if __name__ == "__main__":
    Core().run()
    scenario = tp.create_scenario(scenario_cfg)
    Gui(page).run()
