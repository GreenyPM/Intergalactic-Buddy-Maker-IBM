import os
import keyboard
from openai import OpenAI
import cv2
import base64

class animeAI:
  def __init__(self):
    self.finalPrompt = ""
    self.add1 = "Intergalactic Attractive Waifu"
    self.thing1 = "With red armor"
    self.thing2 = "has green skin"
    self.counter = 0
<<<<<<< Updated upstream
    self.client = OpenAI(api_key = "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")
=======
    self.client = OpenAI(api_key = "API-KEY-HERE")
>>>>>>> Stashed changes

  def typeEntry(self, a):
    self.add1 = a

  def phraseEntry(self, a):
    self.thing1 = a

  def objEntry(self, a):
    self.thing2 = a

  def finalPromptGenerator(self,basePrompt):
    #Remeber the basePrompt has to be list.
    basePrompt.insert(2, self.add1)
    basePrompt.insert(4, self.thing1)
    basePrompt.insert(6, self.thing2)
    for i in basePrompt:
      self.finalPrompt += i
        #rename potentially
    return self.finalPrompt

  def generate(self):
  #Keep this Hidden
    #__payKey =self.client.api_key = "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"

  #_dont mess with it
  #LIMIT FOR DAY OF IS 100-200 HVE COUNTER CODED!!!

  #The idea is to have the promt be created by making it a list and stuff to it as we go
    response = self.client.images.generate(
      prompt=self.finalPrompt,
      n=1,
      size="512x512",
      response_format="b64_json"
    )
    #This is happening for a reason, fix it... The new update from the 6th of November really fucked us up
    #Link: https://github.com/openai/openai-python/discussions/742
    #image_b64 = response['data'][0]['b64_json']
    image_b64 = response.data[0].b64_json
    imgUncode = base64.b64decode(image_b64)
    self.counter += 1
    fh = open("Images\\img{}.png".format(self.counter), "wb")
    fh.write(imgUncode)
    fh.close()
    return 0




#cv2.imwrite("V:\\Python Personal\\GOW2\\testImg\\text.png", imagefinal)