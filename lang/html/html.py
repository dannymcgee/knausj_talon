from talon import Module, Context, actions, ui, imgui, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.html
mode: command
and code.language: html
"""


@mod.action_class
class user_html_code_actions:
    def code_markup_tag(text: str):
        """Inserts an HTML tag"""

    def code_markup_tag_self_closing(text: str):
        """Inserts a self-closing HTML tag"""

    def code_attr(text: str):
        """Inserts an `attribute="value"` pair"""

    def code_bind_property(text: str):
        """Inserts an Angular property binding"""

    def code_bind_event(text: str):
        """Inserts an Angular event binding"""

    def code_local_ref(text: str):
        """Inserts an Angular template local reference"""


@ctx.action_class("user")
class user_actions:
    def code_markup_tag(text: str):
        tag_name = actions.user.formatted_text(text, "DASH_SEPARATED")
        actions.user.paste("<{}></{}>".format(tag_name, tag_name))

        for _ in range(len(tag_name.split("-"))):
            actions.edit.word_left()

        for _ in range(2):
            actions.edit.left()


    def code_markup_tag_self_closing(text: str):
        tag_name = actions.user.formatted_text(text, "DASH_SEPARATED")
        actions.user.paste("<{} />".format(tag_name))
        actions.edit.word_left()


    def code_attr(text: str):
        attr_name = actions.user.formatted_text(text, "DASH_SEPARATED")
        actions.user.paste('{}=""'.format(attr_name))
        actions.edit.left()


    def code_bind_property(text: str):
        if text:
            prop_name = actions.user.formatted_text(text, "PRIVATE_CAMEL_CASE")
            actions.user.paste('[{}]=""'.format(prop_name))
            actions.edit.left()
        else:
            actions.user.paste('[]=""')
            for _ in range(4):
                actions.edit.left()


    def code_bind_event(text: str):
        if text:
            prop_name = actions.user.formatted_text(text, "PRIVATE_CAMEL_CASE")
            actions.user.paste('({})=""'.format(prop_name))
            actions.edit.left()
        else:
            actions.user.paste('()=""')
            for _ in range(4):
                actions.edit.left()


    def code_local_ref(text: str):
        ref_name = actions.user.formatted_text(text, "PRIVATE_CAMEL_CASE")
        actions.user.paste("#" + ref_name)


    def code_default_function(text: str):
        func_name = actions.user.formatted_text(text, "PRIVATE_CAMEL_CASE")
        actions.user.paste(func_name + "()")
        actions.edit.left()
