
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '51D644FE78ADCEDE08E2E4EEFE6045B0'
    
_lr_action_items = {'$end':([1,7,8,],[0,-1,-3,]),'NUM':([4,6,],[-2,8,]),'SIMB':([2,3,4,5,],[4,-4,-2,4,]),'LET':([0,],[3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ast':([0,],[1,]),'num':([6,],[7,]),'let':([0,],[2,]),'simb':([2,5,],[5,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ast","S'",1,None,None,None),
  ('ast -> let simb simb num','ast',4,'p_ast','yacc.py',206),
  ('simb -> SIMB','simb',1,'p_simbol','yacc.py',215),
  ('num -> NUM','num',1,'p_num','yacc.py',223),
  ('let -> LET','let',1,'p_let','yacc.py',251),
]
