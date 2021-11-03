
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftIGUALDADDIFERENTEleftMENORMAYORMAYORIMENORIleftMASMENOSCOMAleftPORDIVMODleftPARIPARDleftPOTAND CADENA COMA CORD CORI DECIMAL DIFERENTE DIV DPUNTOS ENTERO ID IGUAL IGUALDAD LLD LLI MAS MAYOR MAYORI MENOR MENORI MENOS MOD OR PARD PARI POR POT PTCOMA PUNTO RFLOAT RFMT RFUNC RGOTO RIF RIMPORT RINT RMATH RMOD RPACKAGE RPRINTF RRETURN RVARinit : RPACKAGE ID PTCOMA imports declaraciones L_codigoinit : RPACKAGE ID PTCOMA declaraciones L_codigoimports : imports importimports : importimport : RIMPORT PARI CADENA PARD PTCOMAdeclaraciones : declaraciones declaraciondeclaraciones : declaraciondeclaracion : RVAR temp_list CORI ENTERO CORD RFLOAT PTCOMAdeclaracion : RVAR temp_list tipo PTCOMAtemp_list : temp_list COMA IDtemp_list : IDtipo : RINT\n            | RFLOATL_codigo : L_codigo codigoL_codigo : codigocodigo : codecode : RFUNC ID PARI PARD instruccionesinstrucciones : LLI instrucciones_2 LLDinstrucciones_2 : instrucciones_2 instruccion\n                        | instruccioninstruccion  : asignacion PTCOMA\n                    | label DPUNTOS\n                    | gotoS PTCOMA\n                    | llamada_funcion PTCOMA\n                    | cond_if\n                    | returnE PTCOMA\n                    | printF PTCOMA\n                    label : IDgotoS : RGOTO IDreturnE : RRETURNprintF : RFMT PUNTO RPRINTF PARI CADENA COMA valor PARDvalor : RINT PARI expresion PARD\n            |   expresioncond_if : RIF expresion LLI RGOTO ID PTCOMA LLDaccess :   ID CORI RINT PARI expresion PARD CORD\n                | ID CORI expresion CORDasignacion : access IGUAL expresionasignacion :   ID IGUAL expresion\n                | ID IGUAL accessllamada_funcion : ID PARI PARDexpresion : expresion MAS expresion\n                  | expresion MENOS expresion\n                  | expresion POR expresion\n                  | expresion DIV expresion\n                  | expresion OR expresion\n                  | expresion AND expresion\n                  | expresion IGUALDAD expresion\n                  | expresion DIFERENTE expresion\n                  | expresion MAYOR expresion\n                  | expresion MENOR expresion\n                  | expresion MAYORI expresion\n                  | expresion MENORI expresion\n                  | expresion POT expresion\n                  | expresion MOD expresionexpresion : PARI expresion PARDexpresion : ENTERO\n                |   ID\n                |   MENOS ENTERO\n                |   DECIMALexpresion : RMATH PUNTO RMOD PARI expresion COMA expresion PARD'
    
_lr_action_items = {'RPACKAGE':([0,],[2,]),'$end':([1,13,15,16,21,22,38,57,],[0,-2,-15,-16,-1,-14,-17,-18,]),'ID':([2,10,17,28,39,41,42,47,52,53,58,59,60,61,62,63,64,65,66,68,73,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,106,126,131,133,134,140,],[3,20,23,34,51,51,-20,-25,69,71,-19,-21,-22,-23,-24,-26,-27,71,79,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,125,71,71,-34,71,71,]),'PTCOMA':([3,26,27,29,31,40,43,45,46,48,49,54,69,71,74,75,78,79,80,81,82,100,105,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,125,132,139,141,],[4,-13,33,-12,36,56,59,61,62,63,64,-30,-29,-57,-56,-59,-37,-57,-38,-39,-40,-58,-36,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,129,-35,-31,-60,]),'RIMPORT':([4,5,7,12,36,],[9,9,-4,-3,-5,]),'RVAR':([4,5,6,7,8,11,12,14,33,36,56,],[10,10,10,-4,-7,10,-3,-6,-9,-5,-8,]),'RFUNC':([6,8,11,13,14,15,16,21,22,33,38,56,57,],[17,-7,17,17,-6,-15,-16,17,-14,-9,-17,-8,-18,]),'PARI':([9,23,51,53,65,66,68,73,83,86,87,88,89,90,91,92,93,94,95,96,97,98,99,103,104,122,126,131,134,136,140,],[18,30,67,73,73,73,73,73,104,73,73,73,73,73,73,73,73,73,73,73,73,73,73,123,73,126,73,73,73,140,73,]),'CADENA':([18,123,],[24,127,]),'CORI':([19,20,34,51,79,],[25,-11,-10,68,68,]),'COMA':([19,20,34,71,74,75,100,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,127,130,141,],[28,-11,-10,-57,-56,-59,-58,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,131,134,-60,]),'RINT':([19,20,34,68,131,],[29,-11,-10,83,136,]),'RFLOAT':([19,20,34,37,],[26,-11,-10,40,]),'PARD':([24,30,67,71,74,75,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,135,137,138,141,142,143,],[31,35,82,-57,-56,-59,-58,121,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,128,139,-33,141,-60,143,-32,]),'ENTERO':([25,53,65,66,68,72,73,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,126,131,134,140,],[32,74,74,74,74,100,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'CORD':([32,71,74,75,84,100,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,128,141,],[37,-57,-56,-59,105,-58,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,132,-60,]),'LLI':([35,70,71,74,75,100,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,141,],[39,85,-57,-56,-59,-58,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-60,]),'RGOTO':([39,41,42,47,58,59,60,61,62,63,64,85,133,],[52,52,-20,-25,-19,-21,-22,-23,-24,-26,-27,106,-34,]),'RIF':([39,41,42,47,58,59,60,61,62,63,64,133,],[53,53,-20,-25,-19,-21,-22,-23,-24,-26,-27,-34,]),'RRETURN':([39,41,42,47,58,59,60,61,62,63,64,133,],[54,54,-20,-25,-19,-21,-22,-23,-24,-26,-27,-34,]),'RFMT':([39,41,42,47,58,59,60,61,62,63,64,133,],[55,55,-20,-25,-19,-21,-22,-23,-24,-26,-27,-34,]),'LLD':([41,42,47,58,59,60,61,62,63,64,129,133,],[57,-20,-25,-19,-21,-22,-23,-24,-26,-27,133,-34,]),'DPUNTOS':([44,51,],[60,-28,]),'IGUAL':([50,51,105,132,],[65,66,-36,-35,]),'MENOS':([53,65,66,68,70,71,73,74,75,78,79,80,84,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,126,130,131,134,137,138,140,141,142,],[72,72,72,72,87,-57,72,-56,-59,87,-57,87,87,72,72,72,72,72,72,72,72,72,72,72,72,72,72,-58,87,72,-41,-42,-43,-44,87,87,87,87,87,87,87,87,-53,-54,-55,87,72,87,72,72,87,87,72,-60,87,]),'DECIMAL':([53,65,66,68,73,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,126,131,134,140,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'RMATH':([53,65,66,68,73,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,126,131,134,140,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'PUNTO':([55,76,],[77,102,]),'MAS':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[86,-57,-56,-59,86,-57,86,86,-58,86,-41,-42,-43,-44,86,86,86,86,86,86,86,86,-53,-54,-55,86,86,86,86,-60,86,]),'POR':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[88,-57,-56,-59,88,-57,88,88,-58,88,88,88,-43,-44,88,88,88,88,88,88,88,88,-53,-54,-55,88,88,88,88,-60,88,]),'DIV':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[89,-57,-56,-59,89,-57,89,89,-58,89,89,89,-43,-44,89,89,89,89,89,89,89,89,-53,-54,-55,89,89,89,89,-60,89,]),'OR':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[90,-57,-56,-59,90,-57,90,90,-58,90,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,90,90,90,90,-60,90,]),'AND':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[91,-57,-56,-59,91,-57,91,91,-58,91,-41,-42,-43,-44,91,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,91,91,91,91,-60,91,]),'IGUALDAD':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[92,-57,-56,-59,92,-57,92,92,-58,92,-41,-42,-43,-44,92,92,-47,-48,-49,-50,-51,-52,-53,-54,-55,92,92,92,92,-60,92,]),'DIFERENTE':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[93,-57,-56,-59,93,-57,93,93,-58,93,-41,-42,-43,-44,93,93,-47,-48,-49,-50,-51,-52,-53,-54,-55,93,93,93,93,-60,93,]),'MAYOR':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[94,-57,-56,-59,94,-57,94,94,-58,94,-41,-42,-43,-44,94,94,94,94,-49,-50,-51,-52,-53,-54,-55,94,94,94,94,-60,94,]),'MENOR':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[95,-57,-56,-59,95,-57,95,95,-58,95,-41,-42,-43,-44,95,95,95,95,-49,-50,-51,-52,-53,-54,-55,95,95,95,95,-60,95,]),'MAYORI':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[96,-57,-56,-59,96,-57,96,96,-58,96,-41,-42,-43,-44,96,96,96,96,-49,-50,-51,-52,-53,-54,-55,96,96,96,96,-60,96,]),'MENORI':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[97,-57,-56,-59,97,-57,97,97,-58,97,-41,-42,-43,-44,97,97,97,97,-49,-50,-51,-52,-53,-54,-55,97,97,97,97,-60,97,]),'POT':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[98,-57,-56,-59,98,-57,98,98,-58,98,98,98,98,98,98,98,98,98,98,98,98,98,-53,98,-55,98,98,98,98,-60,98,]),'MOD':([70,71,74,75,78,79,80,84,100,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,124,130,137,138,141,142,],[99,-57,-56,-59,99,-57,99,99,-58,99,99,99,-43,-44,99,99,99,99,99,99,99,99,-53,-54,-55,99,99,99,99,-60,99,]),'RPRINTF':([77,],[103,]),'RMOD':([102,],[122,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'imports':([4,],[5,]),'declaraciones':([4,5,],[6,11,]),'import':([4,5,],[7,12,]),'declaracion':([4,5,6,11,],[8,8,14,14,]),'L_codigo':([6,11,],[13,21,]),'codigo':([6,11,13,21,],[15,15,22,22,]),'code':([6,11,13,21,],[16,16,16,16,]),'temp_list':([10,],[19,]),'tipo':([19,],[27,]),'instrucciones':([35,],[38,]),'instrucciones_2':([39,],[41,]),'instruccion':([39,41,],[42,58,]),'asignacion':([39,41,],[43,43,]),'label':([39,41,],[44,44,]),'gotoS':([39,41,],[45,45,]),'llamada_funcion':([39,41,],[46,46,]),'cond_if':([39,41,],[47,47,]),'returnE':([39,41,],[48,48,]),'printF':([39,41,],[49,49,]),'access':([39,41,66,],[50,50,81,]),'expresion':([53,65,66,68,73,86,87,88,89,90,91,92,93,94,95,96,97,98,99,104,126,131,134,140,],[70,78,80,84,101,107,108,109,110,111,112,113,114,115,116,117,118,119,120,124,130,137,138,142,]),'valor':([131,],[135,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> RPACKAGE ID PTCOMA imports declaraciones L_codigo','init',6,'p_init','Optimizador_Sintactico.py',34),
  ('init -> RPACKAGE ID PTCOMA declaraciones L_codigo','init',5,'p_init_2','Optimizador_Sintactico.py',38),
  ('imports -> imports import','imports',2,'p_imports','Optimizador_Sintactico.py',42),
  ('imports -> import','imports',1,'p_imports2','Optimizador_Sintactico.py',47),
  ('import -> RIMPORT PARI CADENA PARD PTCOMA','import',5,'p_import3','Optimizador_Sintactico.py',51),
  ('declaraciones -> declaraciones declaracion','declaraciones',2,'p_declaraciones','Optimizador_Sintactico.py',55),
  ('declaraciones -> declaracion','declaraciones',1,'p_declaraciones2','Optimizador_Sintactico.py',60),
  ('declaracion -> RVAR temp_list CORI ENTERO CORD RFLOAT PTCOMA','declaracion',7,'p_declaraciones3','Optimizador_Sintactico.py',64),
  ('declaracion -> RVAR temp_list tipo PTCOMA','declaracion',4,'p_declaraciones4','Optimizador_Sintactico.py',68),
  ('temp_list -> temp_list COMA ID','temp_list',3,'p_Lista_Temps','Optimizador_Sintactico.py',72),
  ('temp_list -> ID','temp_list',1,'p_Lista_Temps2','Optimizador_Sintactico.py',76),
  ('tipo -> RINT','tipo',1,'p_tipo','Optimizador_Sintactico.py',80),
  ('tipo -> RFLOAT','tipo',1,'p_tipo','Optimizador_Sintactico.py',81),
  ('L_codigo -> L_codigo codigo','L_codigo',2,'p_codigo_1','Optimizador_Sintactico.py',88),
  ('L_codigo -> codigo','L_codigo',1,'p_codigo_2','Optimizador_Sintactico.py',93),
  ('codigo -> code','codigo',1,'p_codigo_3','Optimizador_Sintactico.py',97),
  ('code -> RFUNC ID PARI PARD instrucciones','code',5,'p_codigo_4','Optimizador_Sintactico.py',101),
  ('instrucciones -> LLI instrucciones_2 LLD','instrucciones',3,'p_codigo_5','Optimizador_Sintactico.py',105),
  ('instrucciones_2 -> instrucciones_2 instruccion','instrucciones_2',2,'p_codigo_6','Optimizador_Sintactico.py',109),
  ('instrucciones_2 -> instruccion','instrucciones_2',1,'p_codigo_6','Optimizador_Sintactico.py',110),
  ('instruccion -> asignacion PTCOMA','instruccion',2,'p_codigo_7','Optimizador_Sintactico.py',118),
  ('instruccion -> label DPUNTOS','instruccion',2,'p_codigo_7','Optimizador_Sintactico.py',119),
  ('instruccion -> gotoS PTCOMA','instruccion',2,'p_codigo_7','Optimizador_Sintactico.py',120),
  ('instruccion -> llamada_funcion PTCOMA','instruccion',2,'p_codigo_7','Optimizador_Sintactico.py',121),
  ('instruccion -> cond_if','instruccion',1,'p_codigo_7','Optimizador_Sintactico.py',122),
  ('instruccion -> returnE PTCOMA','instruccion',2,'p_codigo_7','Optimizador_Sintactico.py',123),
  ('instruccion -> printF PTCOMA','instruccion',2,'p_codigo_7','Optimizador_Sintactico.py',124),
  ('label -> ID','label',1,'p_label','Optimizador_Sintactico.py',129),
  ('gotoS -> RGOTO ID','gotoS',2,'p_goto','Optimizador_Sintactico.py',133),
  ('returnE -> RRETURN','returnE',1,'p_return','Optimizador_Sintactico.py',137),
  ('printF -> RFMT PUNTO RPRINTF PARI CADENA COMA valor PARD','printF',8,'p_printF','Optimizador_Sintactico.py',141),
  ('valor -> RINT PARI expresion PARD','valor',4,'p_valor','Optimizador_Sintactico.py',145),
  ('valor -> expresion','valor',1,'p_valor','Optimizador_Sintactico.py',146),
  ('cond_if -> RIF expresion LLI RGOTO ID PTCOMA LLD','cond_if',7,'p_if','Optimizador_Sintactico.py',155),
  ('access -> ID CORI RINT PARI expresion PARD CORD','access',7,'p_access','Optimizador_Sintactico.py',159),
  ('access -> ID CORI expresion CORD','access',4,'p_access','Optimizador_Sintactico.py',160),
  ('asignacion -> access IGUAL expresion','asignacion',3,'p_assign','Optimizador_Sintactico.py',168),
  ('asignacion -> ID IGUAL expresion','asignacion',3,'p_assign2','Optimizador_Sintactico.py',172),
  ('asignacion -> ID IGUAL access','asignacion',3,'p_assign2','Optimizador_Sintactico.py',173),
  ('llamada_funcion -> ID PARI PARD','llamada_funcion',3,'p_llamada_funcion','Optimizador_Sintactico.py',179),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',183),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',184),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',185),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',186),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',187),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',188),
  ('expresion -> expresion IGUALDAD expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',189),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',190),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',191),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',192),
  ('expresion -> expresion MAYORI expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',193),
  ('expresion -> expresion MENORI expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',194),
  ('expresion -> expresion POT expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',195),
  ('expresion -> expresion MOD expresion','expresion',3,'p_expresion_binaria','Optimizador_Sintactico.py',196),
  ('expresion -> PARI expresion PARD','expresion',3,'p_expresion_agrupacion','Optimizador_Sintactico.py',200),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','Optimizador_Sintactico.py',204),
  ('expresion -> ID','expresion',1,'p_expresion_entero','Optimizador_Sintactico.py',205),
  ('expresion -> MENOS ENTERO','expresion',2,'p_expresion_entero','Optimizador_Sintactico.py',206),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_entero','Optimizador_Sintactico.py',207),
  ('expresion -> RMATH PUNTO RMOD PARI expresion COMA expresion PARD','expresion',8,'p_expresion_mod','Optimizador_Sintactico.py',214),
]
