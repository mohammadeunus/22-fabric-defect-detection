

def createSample(sample):
  """
  returns a,b
  where a is the code of the fabric
    and b is the type of defect
  """
  import time
  import random
  import string
  from datetime import datetime

 

  for i in range(sample):
      fabric_id = ''.join(random.choice(string.ascii_letters) for x in range(5))
      now = datetime.now()
      for j in range(random.randint(10, 15)):
          defect_id = random.randint(1, 22)
          yield fabric_id, defect_id , now
          time.sleep(1)
      time.sleep(15)

 