class InfoData:
    def __init__(self, info=[]):
        self.info = []
        self.set_info(info)

    def set_info(self, info):
        if isinstance(info, list):
            self.info.extend(info)
        else:
            self.info.append(info)
        # self.info = PhUtil.to_list(info, trim_data=True, all_str=True)

    def get_info_list(self):
        return self.info

    def get_info_count(self):
        return len(self.info)

    def get_info_str(self, sep='\n\t'):
        return sep.join(filter(None, self.info))
