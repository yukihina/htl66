



















screen _image_selecter(default, string=""):
    key "game_menu" action Return("")
    zorder 20
    for e in default:
        $ string += e + " "
    $ default_set = set(default)
    frame:
        background "#0006"
        xalign 1.
        has vbox
        label _("Type a image name") style "image_selecter_input"

        input default string style "image_selecter_input"
        if default:
            $ s = set()
            for name in renpy.display.image.images:
                $ name_set = set(name)
                if default_set < name_set:
                    $ s.update(name_set-default_set)
                elif default_set == name_set:
                    $ s.update(default_set)
        else:
            $ s = {name[0] for name in renpy.display.image.images}
        viewport:
            mousewheel True
            xmaximum 400


            scrollbars "both"
            has vbox:
                style_group "image_selecter"
            for tag in tuple(s):
                textbutton tag action Return(default + (tag, )) hovered ShowImage(default, tag) unhovered Function(renpy.hide, "preview", layer="screens")










init:
    style image_selecter_input:
        outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    style image_selecter_button:
        size_group "image_selecter"
        idle_background None
    style image_selecter_button_text:
        xalign .0
        outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
init -2000 python:
    def _open_image_viewer():
        if not renpy.config.developer:
            return
        default = ()
        while True:
            name = renpy.invoke_in_new_context(renpy.call_screen, "_image_selecter", default=default)
            if isinstance(name, tuple): 
                default = tuple(name)
            elif name: 
                default = tuple(name.split())
            else:
                renpy.notify(_("Please type image name"))
                return

init -1 python:
    @renpy.pure
    class ShowImage(renpy.store.Action, renpy.store.DictEquality):
        def __init__(self, default, tag):
            self.string=""
            for e in default:
                self.string += e + " "
            self.string += tag
            self.check = None
        
        def __call__(self):
            if self.check is None:
                for n in renpy.display.image.images:
                    if set(n) == set(self.string.split()):
                        self.string=""
                        for e in n:
                            self.string += e + " "
                        try:
                            for fn in renpy.display.image.images[n].predict_files():
                                if not renpy.loader.loadable(fn):
                                    self.check = False
                                    break
                            else:
                                self.check = True
                        except:
                            self.check = True 
            if self.check:
                renpy.show(self.string, at_list=[renpy.store.truecenter], layer="screens", tag="preview")
            else:
                renpy.show("preview", what=renpy.text.text.Text("No files", color="#F00"), at_list=[renpy.store.truecenter], layer="screens")
            renpy.restart_interaction()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
