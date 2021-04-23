mode: user.html
mode: command
and code.language: html
-
tag(): user.code_operators
tag(): user.code_comment
tag(): user.code_generic

# The 'markup' prefix helps to disambiguate from 'tab'
markup tag <user.text>: user.code_markup_tag(text)
markup mini tag <user.text>: user.code_markup_tag_self_closing(text)
markup div: user.code_markup_tag("div")

# Attribute
adder <user.text>: user.code_attr(text)

# Angular-specific stuff
bind property [<user.text>]: user.code_bind_property(text)
bind event [<user.text>]: user.code_bind_event(text)
local ref <user.text>: user.code_local_ref(text)

action(user.code_state_if):
    insert(" *ngIf=\"\"")
    key(left)

action(user.code_state_for_each):
    insert(" *ngFor=\" in \"")
    key(left)
    edit.word_left()
    key(left)

funk <user.text>: user.code_default_function(text)
dollar event: user.paste("$event")
