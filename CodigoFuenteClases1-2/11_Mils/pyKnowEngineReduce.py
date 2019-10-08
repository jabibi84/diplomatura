from pyknow import *

class Segment(Fact):
  """Segment Description."""
  @DefFacts()
  def _initial_action(self):
      yield Fact(GEO_04="AR")
      yield Fact(MNG="CA01")

class InferenceEngine(KnowledgeEngine):
    """Forward Chaining."""

    @Rule(Segment(client='caba'))
    def sgm_caba(self):
        print("CABA")

    @Rule(Segment(client='gba'))
    def sgm_gba(self):
        print("Gran Buenos Aires")

    @Rule(Segment(client='mdz'))
    def sgm_mdz(self):
        print("Mendoza")

    @Rule(Segment(client='slt'))
    def sgm_slt(self):
        print("Salta")

    @Rule('light' << Segment(client=L('yellow') | L('blinking-yellow')))
    def cautious(self, light):
        print("Be cautious because light is", light["color"])


engine = InferenceEngine()
engine.reset()
#engine.declare(Segment(client=choice(['caba', 'yellow', 'blinking-yellow', 'red'])))
engine.declare(Segment(client='caba'))
engine.run()