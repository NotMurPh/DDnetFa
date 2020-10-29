import pyperclip
class FarsiConverter():

    lastchar=None
    ConvertedText=''
    UnknwonChars=''
    Farsi=False

    def __init__(self,name,isolated,start,mid,end):
        self.name=name
        self.isolated=isolated
        self.start=start
        self.mid=mid
        self.end=end
        Characters.append(self)

    def BindWord(self):
        #agar char ghabli nadashtim ya char ghabli nemichasbid be badi ya char jadid nemichasbe be ghabli : isole bezar
        if FarsiConverter.lastchar == None or FarsiConverter.lastchar.mid == FarsiConverter.lastchar.end or self.start==self.mid:
            FarsiConverter.ConvertedText+=self.isolated

        #agar hatman lastchar dashtim = vared sho
        if FarsiConverter.lastchar!=None:
            #agar char jadid be ghabli michasbid va char ghabli end bod : char ghabli mishe mid char jadid end
            if self.start!=self.mid and FarsiConverter.ConvertedText[-1]==FarsiConverter.lastchar.end:
                FarsiConverter.ConvertedText=FarsiConverter.ConvertedText[:-1]+FarsiConverter.lastchar.mid+self.end
            #agar char jadid be ghabli michasbid va char ghabli isole bode va be jadid michasbe : char ghabli start she jadid end she
            if self.start!=self.mid and FarsiConverter.ConvertedText[-1]==FarsiConverter.lastchar.isolated and FarsiConverter.lastchar.mid!=FarsiConverter.lastchar.end:
                FarsiConverter.ConvertedText=FarsiConverter.ConvertedText[:-1]+FarsiConverter.lastchar.start+self.end

        FarsiConverter.lastchar=self

    @staticmethod
    def AddUnknownChars():
        AllNonChar=False
        if len(FarsiConverter.UnknwonChars)>0:
            if len(FarsiConverter.UnknwonChars)>1:
                for LastLeftNonChar in range(len(FarsiConverter.UnknwonChars)):
                    if FarsiConverter.UnknwonChars[LastLeftNonChar].isalnum()==True:
                        LastLeftNonChar-=1
                        break
                else:
                    AllNonChar=True

                for LastRightNonChar in range(len(FarsiConverter.UnknwonChars)-1,-1,-1):
                    if FarsiConverter.UnknwonChars[LastRightNonChar].isalnum()==True:
                        LastRightNonChar+=1
                        break

                if FarsiConverter.Farsi==True and AllNonChar==False:
                    FarsiConverter.UnknwonChars=FarsiConverter.UnknwonChars[LastRightNonChar:][::-1]+FarsiConverter.UnknwonChars[LastLeftNonChar+1:LastRightNonChar]+FarsiConverter.UnknwonChars[:LastLeftNonChar+1][::-1]

            if AllNonChar==False:
                FarsiConverter.ConvertedText+=FarsiConverter.UnknwonChars[::-1]
            else:
                FarsiConverter.ConvertedText+=FarsiConverter.UnknwonChars

            FarsiConverter.UnknwonChars=''
            FarsiConverter.lastchar=None

    @staticmethod
    def ReverseAndCopy():
        pyperclip.copy(FarsiConverter.ConvertedText[::-1])
        if __name__ == '__main__':
            print('\n'+FarsiConverter.ConvertedText[::-1]+'\n')
            Manager()

Characters=[]
A1=FarsiConverter(name='ا',isolated='ﺍ',start='ﺍ',mid='ﺎ',end='ﺎ')
B=FarsiConverter(name='ب',isolated='ﺏ',start='ﺑ',mid='ﺒ',end='ﺐ')
P=FarsiConverter(name='پ',isolated='ﭖ',start='ﭘ',mid='ﭙ',end='ﭗ')
T1=FarsiConverter(name='ت',isolated='ﺕ',start='ﺗ',mid='ﺘ',end='ﺖ')
S1=FarsiConverter(name='ث',isolated='ﺙ',start='ﺛ',mid='ﺜ',end='ﺚ')
J=FarsiConverter(name='ج',isolated='ﺝ',start='ﺟ',mid='ﺠ',end='ﺞ')
Ch=FarsiConverter(name='چ',isolated='ﭺ',start='ﭼ',mid='ﭽ',end='ﭻ')
H1=FarsiConverter(name='ح',isolated='ﺡ',start='ﺣ',mid='ﺤ',end='ﺢ')
Kh=FarsiConverter(name='خ',isolated='ﺥ',start='ﺧ',mid='ﺨ',end='ﺦ')
D=FarsiConverter(name='د',isolated='ﺩ',start='ﺩ',mid='ﺪ',end='ﺪ')
Z1=FarsiConverter(name='ذ',isolated='ﺫ',start='ﺫ',mid='ﺬ',end='ﺬ')
R=FarsiConverter(name='ر',isolated='ﺭ',start='ﺭ',mid='ﺮ',end='ﺮ')
Z2=FarsiConverter(name='ز',isolated='ﺯ',start='ﺯ',mid='ﺰ',end='ﺰ')
Jh=FarsiConverter(name='ژ',isolated='ﮊ',start='ﮊ',mid='ﮋ',end='ﮋ')
S2=FarsiConverter(name='س',isolated='ﺱ',start='ﺳ',mid='ﺴ',end='ﺲ')
Sh=FarsiConverter(name='ش',isolated='ﺵ',start='ﺷ',mid='ﺸ',end='ﺶ')
S3=FarsiConverter(name='ص',isolated='ﺹ',start='ﺻ',mid='ﺼ',end='ﺺ')
Z3=FarsiConverter(name='ض',isolated='ﺽ',start='ﺿ',mid='ﻀ',end='ﺾ')
T2=FarsiConverter(name='ط',isolated='ﻁ',start='ﻃ',mid='ﻄ',end='ﻂ')
Z4=FarsiConverter(name='ظ',isolated='ﻅ',start='ﻇ',mid='ﻈ',end='ﻆ')
A2=FarsiConverter(name='ع',isolated='ﻉ',start='ﻋ',mid='ﻌ',end='ﻊ')
Gh1=FarsiConverter(name='غ',isolated='ﻍ',start='ﻏ',mid='ﻐ',end='ﻎ')
F=FarsiConverter(name='ف',isolated='ﻑ',start='ﻓ',mid='ﻔ',end='ﻒ')
Gh2=FarsiConverter(name='ق',isolated='ﻕ',start='ﻗ',mid='ﻘ',end='ﻖ')
K=FarsiConverter(name='ک',isolated='ﮎ',start='ﮐ',mid='ﮑ',end='ﮏ')
G=FarsiConverter(name='گ',isolated='ﮒ',start='ﮔ',mid='ﮕ',end='ﮓ')
L=FarsiConverter(name='ل',isolated='ﻝ',start='ﻟ',mid='ﻠ',end='ﻞ')
M=FarsiConverter(name='م',isolated='ﻡ',start='ﻣ',mid='ﻤ',end='ﻢ')
N=FarsiConverter(name='ن',isolated='ﻥ',start='ﻧ',mid='ﻨ',end='ﻦ')
V=FarsiConverter(name='و',isolated='ﻭ',start='ﻭ',mid='ﻮ',end='ﻮ')
H2=FarsiConverter(name='ه',isolated='ﻩ',start='ﻫ',mid='ﻬ',end='ﻪ')
Y=FarsiConverter(name='ی',isolated='ﻯ',start='ﻳ',mid='ﻴ',end='ﻰ')

def Manager(input_text=None):
    FarsiConverter.lastchar=None
    FarsiConverter.ConvertedText=''
    FarsiConverter.UnknwonChars=''
    FarsiConverter.Farsi=False

    if __name__ == '__main__':
        input_text=input('Enter Your Persian Text : ')

    for each_char in input_text:
        for each_object in Characters:
            if each_char == each_object.name:
                FarsiConverter.Farsi=True
                FarsiConverter.AddUnknownChars()
                each_object.BindWord()
                break
        else:
            FarsiConverter.UnknwonChars+=each_char
    else:
        FarsiConverter.AddUnknownChars()
        FarsiConverter.ReverseAndCopy()

if __name__ == '__main__':
    Manager()