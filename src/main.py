import pandas as pd


class Convertor:
    def __init__(self, file_path: str, outputname: str = 'output'):
        self.df = pd.read_csv(file_path)
        self.ouputname = outputname

    def convert_to_xlsx(self):
        self.df.to_excel(self.ouputname + '.xlsx')
    
    def convert_to_json(self):
        self.df.to_json(self.ouputname + '.json')
    
    def convert_to_markdown(self):
        self.df.to_markdown(self.ouputname + '.md')


def main():
    file_path = str(input('Selectable csv file path: '))
    extension = str(input('Convert to: ')).split('.')[-1]
    
    try:
        outputname = file_path.split('/')[-1].split('.')[-2]
    except:
        print('File extension not specified!')
        return

    try:
        conv = Convertor(file_path=file_path, outputname=outputname)
    except:
        print('I cant find this file..')
        return
    
    if extension == 'xlsx':
        conv.convert_to_xlsx()
    elif extension == 'json':
        conv.convert_to_json()
    elif extension == 'md':
        conv.convert_to_markdown()
    else:
        print('Whoops... Please choice a correct extension for file.')
        return
    print('Done! File Converted and saved!')

if __name__ == '__main__':
    main()
    
