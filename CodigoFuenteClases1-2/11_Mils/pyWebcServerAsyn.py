import tornado.web
from tornado.ioloop import IOLoop
from tornado import gen
from pyknow import *
from random import choice

class Segment(Fact):
  """Segment Description."""
  @DefFacts()
  def _initial_action(self):
      #Definiciones comunes para el modelo
      yield Fact(GEO_04="AR")


class InferenceEngine(KnowledgeEngine):
    """Tipo de encadenamiento: Forward Chaining."""
    global result
    result = ""

    def getInference(self):
        return result

    @Rule(Fact(sgm='A01'))
    def sgm_a01(self):
        """Definir acciones para el segmento.
           Por ejemplo: Acceder a base de datos.
                        Activar Proceso.
        """
        global result
        result = "A01"

    @Rule(Fact(sgm='A02'))
    def sgm_a02(self):
        """Definir acciones para el segmento.
           Por ejemplo: Acceder a base de datos.
                        Activar Proceso.
        """
        global result
        result = "A02"

    @Rule(OR(Fact(sgm='A03'), (Fact(sgm='A04'))))
    def sgm_a03(self):
        """Definir acciones para el segmento.
           Por ejemplo: Acceder a base de datos.
                        Activar Proceso.
        """
        global result
        result = "A03"

    @Rule(AND(Fact(sgm='A05') , NOT(Fact(GEO_04="BR"))))
    def sgm_a05_AR(self):
        """Definir acciones para el segmento.
           Por ejemplo: Acceder a base de datos.
                        Activar Proceso.
        """
        global result
        result = "A05"

    @Rule(AND(Fact(sgm='A06') , Fact(MNG="MA01")))
    def sgm_a06_AR(self):
        """Definir acciones para el segmento.
           Por ejemplo: Acceder a base de datos.
                        Activar Proceso.
        """
        global result
        result = "A06"

class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        idUser = self.get_argument('id', '0')
        """
        Aqui se simula el acceso a la base de datos para acceder al
        segmento al que pertenece el cliente
        """
        bfSegment = choice(['A01', 'A02', 'A03', 'A04', 'A05', 'A06'])

        engine = InferenceEngine()
        engine.reset()
        engine.declare(Fact(sgm= bfSegment), Fact(MNG="MA01"))
        engine.run()
        self.write("Accion: " + str(engine.getInference()))
        self.finish()

application = tornado.web.Application([(r"/", MainHandler),])

if __name__ == "__main__":
    application.listen(8888)
    IOLoop.instance().start()
