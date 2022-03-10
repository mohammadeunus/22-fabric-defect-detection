def createSample(sample):
    """
    returns a,b
    where a is the code of the fabric
      and b is the type of defect
    """
    import time
    import random
    import string
    NN = ""

    for i in range(sample):
        NN = ''.join(random.choice(string.ascii_letters) for x in range(5))
        for j in range(random.randint(10, 15)):
            n = random.randint(0, 22)
            yield NN, n
            time.sleep(1)
        time.sleep(15)