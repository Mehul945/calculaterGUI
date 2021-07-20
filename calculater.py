# calculaterGUI






from kivy.app import App
from kivy.core import text
from kivy.uix.behaviors import button
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

class MY_Calculater(App):
	def _1(self,instance):
		self.Textinput.text+="1"
	def _2(self,instance):
		self.Textinput.text+="2"
	def _3(self,instance):
		self.Textinput.text+="3"
	def _4(self,instance):
		self.Textinput.text+="4"
	def _5(self,instance):
		self.Textinput.text+="5"
	def _6(self,instance):
		self.Textinput.text+="6"
	def _7(self,instance):
		self.Textinput.text+="7"
	def _8(self,instance):
		self.Textinput.text+="8"
	def _9(self,instance):
		self.Textinput.text+="9"
	def _0(self,instance):
		self.Textinput.text+="0"
	def _p(self,instance):
		self.Textinput.text+=" + "
	def _m(self,instance):
		self.Textinput.text+=" - "
	def _mul(self,instance):
		self.Textinput.text+=" x "
	def _div(self,instance):
		self.Textinput.text+=" / "
	def ans(self,instance):
		rm=str(self.Textinput.text).replace(" ",'').replace("x",'*')
		# rm=str(self.Textinput.text).replace("x",'*')
		try:
			self.Textinput.text=str(eval(rm))
		except Exception as e:
			self.Textinput.text="ERROR"
	def back(self,instance):
		self.Textinput.text=''.join(list(self.Textinput.text)[:-2])
	def clear(self,instance):
		self.Textinput.text=''
	def build(self):
		self.screen=Screen()
		self.Textinput=TextInput(size_hint=(1,.15),font_size="30",pos_hint={"center_x":.5,"center_y":.9},multiline=False)
		self.btn1=Button(text="1",pos_hint={"center_x":.1,"center_y":.7},size_hint=(.15,.15))
		self.btn2=Button(text="2",pos_hint={"center_x":.3,"center_y":.7},size_hint=(.15,.15))
		self.btn3=Button(text="3",pos_hint={"center_x":.5,"center_y":.7},size_hint=(.15,.15))
		self.btn4=Button(text="4",pos_hint={"center_x":.1,"center_y":.5},size_hint=(.15,.15))
		self.btn5=Button(text="5",pos_hint={"center_x":.3,"center_y":.5},size_hint=(.15,.15))
		self.btn6=Button(text="6",pos_hint={"center_x":.5,"center_y":.5},size_hint=(.15,.15))
		self.btn7=Button(text="7",pos_hint={"center_x":.1,"center_y":.3},size_hint=(.15,.15))
		self.btn8=Button(text="8",pos_hint={"center_x":.3,"center_y":.3},size_hint=(.15,.15))
		self.btn9=Button(text="9",pos_hint={"center_x":.5,"center_y":.3},size_hint=(.15,.15))
		self.btn0=Button(text="0",pos_hint={"center_x":.3,"center_y":.1},size_hint=(.15,.15))
		self.btnp=Button(text="+",pos_hint={"center_x":.7,"center_y":.7},size_hint=(.15,.15))
		self.btnm=Button(text="-",pos_hint={"center_x":.9,"center_y":.7},size_hint=(.15,.15))
		self.btnmul=Button(text="X",pos_hint={"center_x":.7,"center_y":.5},size_hint=(.15,.15))
		self.btndiv=Button(text="/",pos_hint={"center_x":.9,"center_y":.5},size_hint=(.15,.15))
		self.btnans=Button(text="=",pos_hint={"center_x":.7,"center_y":.3},size_hint=(.15,.15))
		self.btnback=Button(text="<--",pos_hint={"center_x":.9,"center_y":.3},size_hint=(.15,.15))
		self.btnclear=Button(text="AC",pos_hint={"center_x":.9,"center_y":.1},size_hint=(.15,.15))
		self.btn1.bind(on_press=self._1)
		self.btn2.bind(on_press=self._2)
		self.btn3.bind(on_press=self._3)
		self.btn4.bind(on_press=self._4)
		self.btn5.bind(on_press=self._5)
		self.btn6.bind(on_press=self._6)
		self.btn7.bind(on_press=self._7)
		self.btn8.bind(on_press=self._8)
		self.btn9.bind(on_press=self._9)
		self.btn0.bind(on_press=self._0)
		self.btnp.bind(on_press=self._p)
		self.btnm.bind(on_press=self._m)
		self.btnmul.bind(on_press=self._mul)
		self.btndiv.bind(on_press=self._div)
		self.btnans.bind(on_press=self.ans)
		self.btnback.bind(on_press=self.back)
		self.btnclear.bind(on_press=self.clear)
		# self.btn1.bind(on_press=self.btn1)
		self.screen.add_widget(self.btn1)
		self.screen.add_widget(self.btn2)
		self.screen.add_widget(self.btn3)
		self.screen.add_widget(self.btn4)
		self.screen.add_widget(self.btn5)
		self.screen.add_widget(self.btn6)
		self.screen.add_widget(self.btn7)
		self.screen.add_widget(self.btn8)
		self.screen.add_widget(self.btn9)
		self.screen.add_widget(self.btn0)
		self.screen.add_widget(self.btnp)
		self.screen.add_widget(self.btnm)
		self.screen.add_widget(self.btnmul)
		self.screen.add_widget(self.btndiv)
		self.screen.add_widget(self.btnans)
		self.screen.add_widget(self.btnback)
		self.screen.add_widget(self.btnclear)
		self.screen.add_widget(self.Textinput)
		return self.screen
if __name__=="__main__":
    x=MY_Calculater()
    x.run()
