# -*- coding: utf-8 -*-
from yacc import yacc, lisp_str
import cmd


class MiniLisp(cmd.Cmd):     # See https://docs.python.org/2/library/cmd.html
    """
    MiniLisp evalúa expresiones sencillas con sabor a lisp, 
    más información en http://www.juanjoconti.com.ar
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "ml> "
        self.intro  = "Bienvenido a MiniLisp"

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    def do_EOF(self, args):
        """Exit on system end of file character"""
        print "Good bye!"
        return self.do_exit(args)

    def do_help(self, args):
        print self.__doc__

    def emptyline(self):    
        """Do nothing on empty input line"""
        pass
    
    
    def eval(x):
        "Evaluate an expression in an environment."
        if isinstance(x, Symbol):      # variable reference
            return env.find(x)[x]
        elif not isinstance(x, List):  # constant literal
            return x                
        elif x[0] == 'quote':          # (quote exp)
            (_, exp) = x
            return exp
        elif x[0] == 'if':             # (if test conseq alt)
            (_, test, conseq, alt) = x
            exp = (conseq if eval(test, env) else alt)
            return eval(exp, env)
        elif x[0] == 'define':         # (define var exp)
            (_, var, exp) = x
            env[var] = eval(exp, env)
        elif x[0] == 'let':         # (define var exp)
            (_, var, _, exp) = x
            env[var] = eval(exp, env)
        elif x[0] == 'set!':           # (set! var exp)
            (_, var, exp) = x
            env.find(var)[var] = eval(exp, env)
        elif x[0] == 'lambda':         # (lambda (var...) body)
            (_, parms, body) = x
            return Procedure(parms, body, env)
        else:                          # (proc arg...)
            proc = eval(x[0], env)
            args = [eval(exp, env) for exp in x[1:]]
            return proc(*args)

    def default(self, line):       
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code.
        """
        result = yacc.parse(line)
        print "result is: ", result
        import lis
        print lis.eval(result)
        
#        s = lisp_str(result)
#        if s != 'nil':
#            print s


if __name__ == '__main__':
        ml = MiniLisp()
        
        print "Stream Operations: "
        import ListComprehension
        print "\n"
        
        
        ml.cmdloop()     # See https://docs.python.org/2/library/cmd.html
