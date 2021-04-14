from production.chocolate import Chocolate
from production.packaging import Packaging
from production.batch import Batch

choco1 = Chocolate(name = "Smi")
choco2 = Chocolate(name = "Mint")

pack1 = Packaging(kind = "single")
pack2 = Packaging(kind = "løsvekt")

batch1 = Batch(name = choco1.name, kind = pack1.kind, date = "2021-02-28", boxes = 999)
batch2 = Batch(name = choco2.name, kind = pack2.kind, date = "2021-03-03", boxes = 2000)

#from main import choco1, choco2
#from main import pack1, pack2
#from main import batch1, bacht2