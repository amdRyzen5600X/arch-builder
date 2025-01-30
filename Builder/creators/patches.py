import os

class PatchSystemBugs:
    @staticmethod
    def enable_all_patches():
        PatchSystemBugs.__make_zsh_the_default()
        PatchSystemBugs.__assign_permissions_to_configs()

    @staticmethod
    def __make_zsh_the_default():
        os.system("chsh -s /usr/bin/zsh")

    @staticmethod
    def __assign_permissions_to_configs():
        os.system("sudo chmod -R 700 ~/.config/*")
