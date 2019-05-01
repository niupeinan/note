```pillow
from PIL import Image
im = Image.open("hopper.ppm")
```

```pillow
from PIL import Image.ImageDraw
Image.new("RGB",(100,100),color=(255,0,0))
draw = ImageDraw.Draw(im)
draw.line(0,0,100,100),fill=(200,200,200),width=10)
import random
for item in range(100):
	draw.point(random.randint(0,100),random.randint(0,100),fill=random.randint(0,100),random.randint(0,100),random.randint(0,100) )
im.show()
```

```pillow
from PIL import Image, ImageDraw, ImageFont
import random
import io

class code:
	def __init__(self):
		self.width=400
		self.height=220
		self.im=None
		self.lineNum=0
		self.pointNum=0
		self.textcon="abcdEFGhiJKLMnopq123456"
		self.coldlen=3


	def randBgColor(self):
		return (random.randint(0,255))


	def create(self):
		self.im = Image.new("RGBA",(self.width,self.height),color=self.randBgColor())


	def lines(self):
		lineNum = self.lineNum or random.randint(10,25)
		draw = ImageDraw.Draw(self.im)
		for item in range(lineNum):
			place=(random.randint(0,self.width),random.randint(0,self.height),random.randint(0,self.width),random.randint(0,self.height))
			draw.line(place,fill=self.randBgColor()),


	def points(self):
		pointNum = self.pointNum or random.randint(80,100)
		point = ImageDraw.Draw(self.im)
		for item in range(pointNum):
			place = (random.randint(0, self.width), random.randint(0, self.height))
			point.point(place, fill=self.randBgColor()),


	def texts(self):
		pass


	def output(self):
		self.create()
		self.lines()
		self.points()
		self.texts()
		bt=io.Bytes()
		self.im.save(bt,"png")
		self.im.show()




codeobj=code()
codeobj.output()

self.str+=letter.lower()

res=make_response(codeobj,output())
session["code"]
res.header["content-type]="image/png"

code =request.form["code"]
if code.lower()!=session.get("code"):
	return redirect("/login")
```

