import os
import pprint

class MatchManager:
    def __init__(self, path) -> None:
        self.path = path
    
    def _get_matched_files_list(self, dir:str) -> list:
        '''Get directory name and return matched file list in it'''
        matched_files_list = []
        files = os.listdir(dir)
        for file in files:
            filename = os.path.splitext(file)[0]
            for match_file in files:
                match_file_name, match_file_extention = os.path.splitext(match_file)
                if match_file == file:
                    continue
                if filename == match_file_name and match_file_extention.lower() == '.json':
                    matched_files_list.append([os.path.join(self.path, dir, file), os.path.join(self.path, dir, match_file)])
        return matched_files_list
        
        
    def print_matched_dict(self) -> None:
        '''Print matched dictionary'''
        matched_dict = {}
        files = os.listdir(self.path)
        dirs = []
        for file in files:
            if os.path.isdir(os.path.join(self.path, file)): dirs.append(os.path.join(self.path, file))
        dirs.sort()
        for dir in dirs:
            if self._get_matched_files_list(dir):
                matched_dict[os.path.basename(dir)] = self._get_matched_files_list(dir)
        pprint.pprint(matched_dict)
    
            
if __name__ == '__main__':
    mm = MatchManager("/tmp/labels")
    mm.print_matched_dict()