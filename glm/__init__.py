
import os
import cppyy

cppyy.add_include_path(os.path.join(os.path.split(__file__)[0], "glm"))

cppyy.cppdef("""
#define GLM_FORCE_SWIZZLE
#include <glm/glm.hpp>
#include <glm/ext.hpp>
""")


def __getattr__(name):
	return getattr(cppyy.gbl.glm, name)


def __dir__():
	return dir(cppyy.gbl.glm)