from pyknow import *

engine = KnowledgeEngine()
engine.reset()
engine.declare(Fact(score=5))
engine.facts