'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_draw_elements_base_vertex'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_draw_elements_base_vertex',False)

@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLint)
def glDrawElementsBaseVertex( mode,count,type,indices,basevertex ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLint)
def glDrawRangeElementsBaseVertex( mode,start,end,count,type,indices,basevertex ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei,_cs.GLint)
def glDrawElementsInstancedBaseVertex( mode,count,type,indices,primcount,basevertex ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLsizeiArray,_cs.GLenum,arrays.GLvoidpArray,_cs.GLsizei,arrays.GLintArray)
def glMultiDrawElementsBaseVertex( mode,count,type,indices,primcount,basevertex ):pass


def glInitDrawElementsBaseVertexARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
