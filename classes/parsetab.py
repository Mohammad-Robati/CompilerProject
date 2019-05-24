
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftTHENleftELSEleftORleftANDleftLTleftGTleftGEleftNEleftEQleftLEleftSUMSUBleftMULDIVAND ASSIGN BEGIN BOOL CASE CLOSE_PAREN COLON DIV DO DOWNTO ELSE END EQ FALSE FOR FUNCTION GE GT ID IF INT INTEGER LE LT MUL NE OPEN_PAREN OR PROCEDURE PROGRAM REAL REALNUMBER RETURN SEMI_COLON SEPARATOR SUB SUM THEN TO TRUE WHILEprogram : PROGRAM ID SEMI_COLON declist block SEMI_COLONprogram : PROGRAM ID SEMI_COLON block SEMI_COLONdeclist : decdeclist : declist decdec : vardecdec : procdecdec : funcdectype : INTtype : REALtype : BOOLiddec : IDiddec : ID ASSIGN expidlist : iddecidlist : idlist SEPARATOR iddecvardec : type idlist SEMI_COLONprocdec : PROCEDURE ID OPEN_PAREN paramdecs CLOSE_PAREN declist block SEMI_COLONprocdec : PROCEDURE ID OPEN_PAREN paramdecs CLOSE_PAREN block SEMI_COLONfuncdec : FUNCTION ID OPEN_PAREN paramdecs CLOSE_PAREN COLON type declist block SEMI_COLONfuncdec : FUNCTION ID OPEN_PAREN paramdecs CLOSE_PAREN COLON type block SEMI_COLONparamdecs : paramdecparamdecs : paramdecs SEMI_COLON paramdecparamdec : type paramlistparamlist : IDparamlist : paramlist SEPARATOR IDblock : BEGIN stmtlist ENDblock : stmtstmtlist : stmtstmtlist : stmtlist SEMI_COLON stmtlvalue : IDassignstmt : lvalue ASSIGN expstmt : assignstmtstmt : IF controlifexp THEN blockstmt : IF controlifexp THEN block ELSE controlelse blockcontrolifexp : expcontrolelse : stmt : WHILE controlwhileexp DO blockcontrolwhileexp : expstmt : FOR assignstmt TO controlforupexp DO blockstmt : FOR assignstmt DOWNTO controlfordownexp DO blockcontrolforupexp : expcontrolfordownexp : expstmt : CASE controlcaseexp caseelement ENDcontrolcaseexp : exp caseelement : case COLON caseelementcontrol block SEMI_COLON caseelement : caseelement case COLON caseelementcontrol block SEMI_COLONcaseelementcontrol : case : INTEGERstmt : RETURN expstmt : expexp : exp SUM expexp : exp SUB expexp : exp MUL expexp : exp DIV expexp : exp AND expexp : exp OR expexp : exp NE expexp : exp EQ expexp : exp LT expexp : exp GT expexp : exp LE expexp : exp GE expexp : OPEN_PAREN exp CLOSE_PARENexp : REALNUMBERexp : INTEGERexp : TRUEexp : FALSEexp : lvalueexp : ID OPEN_PAREN explist CLOSE_PARENexplist : expexplist : explist SEPARATOR exp'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,36,71,],[0,-2,-1,]),'ID':([2,4,6,8,9,11,12,13,15,16,17,18,19,21,22,23,24,30,31,32,33,35,50,51,52,53,54,55,56,57,58,59,60,61,68,73,74,75,76,77,93,94,95,101,111,116,119,120,121,122,123,124,129,132,134,137,143,145,147,148,151,152,],[3,5,5,-3,5,-5,-6,-7,5,5,46,5,5,64,65,5,67,-8,-9,-10,5,-4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-15,64,5,5,-46,127,-35,5,5,-46,5,5,5,5,5,144,-17,5,-16,5,-19,-18,]),'SEMI_COLON':([3,5,7,10,14,20,25,26,27,28,29,34,37,38,41,49,62,63,64,72,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,102,103,104,109,112,113,114,115,117,126,127,130,131,133,135,136,139,140,142,144,149,150,],[4,-29,36,-26,-31,-49,-67,-63,-64,-65,-66,71,73,-27,-67,-48,93,-13,-11,-25,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-30,-68,-28,-32,-36,-42,-14,-12,125,-20,125,-22,-23,-38,-39,141,143,-21,-33,146,147,-24,151,152,]),'BEGIN':([4,6,8,11,12,13,30,31,32,35,74,75,93,111,119,120,121,122,123,124,129,132,134,143,145,147,148,151,152,],[9,9,-3,-5,-6,-7,-8,-9,-10,-4,9,9,-15,-46,-35,9,9,-46,9,9,9,9,9,-17,9,-16,9,-19,-18,]),'IF':([4,6,8,9,11,12,13,30,31,32,35,73,74,75,93,111,119,120,121,122,123,124,129,132,134,143,145,147,148,151,152,],[15,15,-3,15,-5,-6,-7,-8,-9,-10,-4,15,15,15,-15,-46,-35,15,15,-46,15,15,15,15,15,-17,15,-16,15,-19,-18,]),'WHILE':([4,6,8,9,11,12,13,30,31,32,35,73,74,75,93,111,119,120,121,122,123,124,129,132,134,143,145,147,148,151,152,],[16,16,-3,16,-5,-6,-7,-8,-9,-10,-4,16,16,16,-15,-46,-35,16,16,-46,16,16,16,16,16,-17,16,-16,16,-19,-18,]),'FOR':([4,6,8,9,11,12,13,30,31,32,35,73,74,75,93,111,119,120,121,122,123,124,129,132,134,143,145,147,148,151,152,],[17,17,-3,17,-5,-6,-7,-8,-9,-10,-4,17,17,17,-15,-46,-35,17,17,-46,17,17,17,17,17,-17,17,-16,17,-19,-18,]),'CASE':([4,6,8,9,11,12,13,30,31,32,35,73,74,75,93,111,119,120,121,122,123,124,129,132,134,143,145,147,148,151,152,],[18,18,-3,18,-5,-6,-7,-8,-9,-10,-4,18,18,18,-15,-46,-35,18,18,-46,18,18,18,18,18,-17,18,-16,18,-19,-18,]),'RETURN':([4,6,8,9,11,12,13,30,31,32,35,73,74,75,93,111,119,120,121,122,123,124,129,132,134,143,145,147,148,151,152,],[19,19,-3,19,-5,-6,-7,-8,-9,-10,-4,19,19,19,-15,-46,-35,19,19,-46,19,19,19,19,19,-17,19,-16,19,-19,-18,]),'PROCEDURE':([4,6,8,11,12,13,30,31,32,35,93,124,134,143,145,147,148,151,152,],[22,22,-3,-5,-6,-7,-8,-9,-10,-4,-15,22,22,-17,22,-16,22,-19,-18,]),'FUNCTION':([4,6,8,11,12,13,30,31,32,35,93,124,134,143,145,147,148,151,152,],[24,24,-3,-5,-6,-7,-8,-9,-10,-4,-15,24,24,-17,24,-16,24,-19,-18,]),'OPEN_PAREN':([4,5,6,8,9,11,12,13,15,16,18,19,23,30,31,32,33,35,50,51,52,53,54,55,56,57,58,59,60,61,65,67,68,73,74,75,76,77,93,95,101,111,119,120,121,122,123,124,129,132,134,143,145,147,148,151,152,],[23,33,23,-3,23,-5,-6,-7,23,23,23,23,23,-8,-9,-10,23,-4,23,23,23,23,23,23,23,23,23,23,23,23,96,98,23,23,23,23,23,23,-15,23,23,-46,-35,23,23,-46,23,23,23,23,23,-17,23,-16,23,-19,-18,]),'REALNUMBER':([4,6,8,9,11,12,13,15,16,18,19,23,30,31,32,33,35,50,51,52,53,54,55,56,57,58,59,60,61,68,73,74,75,76,77,93,95,101,111,119,120,121,122,123,124,129,132,134,143,145,147,148,151,152,],[26,26,-3,26,-5,-6,-7,26,26,26,26,26,-8,-9,-10,26,-4,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-15,26,26,-46,-35,26,26,-46,26,26,26,26,26,-17,26,-16,26,-19,-18,]),'INTEGER':([4,5,6,8,9,11,12,13,15,16,18,19,23,26,27,28,29,30,31,32,33,35,41,47,48,50,51,52,53,54,55,56,57,58,59,60,61,68,73,74,75,76,77,78,81,82,83,84,85,86,87,88,89,90,91,92,93,95,97,100,101,111,119,120,121,122,123,124,129,132,134,141,143,145,146,147,148,151,152,],[27,-29,27,-3,27,-5,-6,-7,27,27,27,27,27,-63,-64,-65,-66,-8,-9,-10,27,-4,-67,80,-43,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,80,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-15,27,-62,-68,27,-46,-35,27,27,-46,27,27,27,27,27,-44,-17,27,-45,-16,27,-19,-18,]),'TRUE':([4,6,8,9,11,12,13,15,16,18,19,23,30,31,32,33,35,50,51,52,53,54,55,56,57,58,59,60,61,68,73,74,75,76,77,93,95,101,111,119,120,121,122,123,124,129,132,134,143,145,147,148,151,152,],[28,28,-3,28,-5,-6,-7,28,28,28,28,28,-8,-9,-10,28,-4,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-15,28,28,-46,-35,28,28,-46,28,28,28,28,28,-17,28,-16,28,-19,-18,]),'FALSE':([4,6,8,9,11,12,13,15,16,18,19,23,30,31,32,33,35,50,51,52,53,54,55,56,57,58,59,60,61,68,73,74,75,76,77,93,95,101,111,119,120,121,122,123,124,129,132,134,143,145,147,148,151,152,],[29,29,-3,29,-5,-6,-7,29,29,29,29,29,-8,-9,-10,29,-4,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-15,29,29,-46,-35,29,29,-46,29,29,29,29,29,-17,29,-16,29,-19,-18,]),'INT':([4,6,8,11,12,13,30,31,32,35,93,96,98,124,125,134,138,143,145,147,148,151,152,],[30,30,-3,-5,-6,-7,-8,-9,-10,-4,-15,30,30,30,30,30,30,-17,30,-16,30,-19,-18,]),'REAL':([4,6,8,11,12,13,30,31,32,35,93,96,98,124,125,134,138,143,145,147,148,151,152,],[31,31,-3,-5,-6,-7,-8,-9,-10,-4,-15,31,31,31,31,31,31,-17,31,-16,31,-19,-18,]),'BOOL':([4,6,8,11,12,13,30,31,32,35,93,96,98,124,125,134,138,143,145,147,148,151,152,],[32,32,-3,-5,-6,-7,-8,-9,-10,-4,-15,32,32,32,32,32,32,-17,32,-16,32,-19,-18,]),'ASSIGN':([5,25,45,46,64,],[-29,68,68,-29,95,]),'SUM':([5,20,25,26,27,28,29,40,41,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,106,108,113,118,],[-29,50,-67,-63,-64,-65,-66,50,-67,50,50,50,50,50,-50,-51,-52,-53,50,50,50,50,50,50,50,50,-62,50,-68,50,50,50,50,]),'SUB':([5,20,25,26,27,28,29,40,41,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,106,108,113,118,],[-29,51,-67,-63,-64,-65,-66,51,-67,51,51,51,51,51,-50,-51,-52,-53,51,51,51,51,51,51,51,51,-62,51,-68,51,51,51,51,]),'MUL':([5,20,25,26,27,28,29,40,41,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,106,108,113,118,],[-29,52,-67,-63,-64,-65,-66,52,-67,52,52,52,52,52,52,52,-52,-53,52,52,52,52,52,52,52,52,-62,52,-68,52,52,52,52,]),'DIV':([5,20,25,26,27,28,29,40,41,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,106,108,113,118,],[-29,53,-67,-63,-64,-65,-66,53,-67,53,53,53,53,53,53,53,-52,-53,53,53,53,53,53,53,53,53,-62,53,-68,53,53,53,53,]),'AND':([5,20,25,26,27,28,29,40,41,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,106,108,113,118,],[-29,54,-67,-63,-64,-65,-66,54,-67,54,54,54,54,54,-50,-51,-52,-53,-54,54,-56,-57,-58,-59,-60,-61,-62,54,-68,54,54,54,54,]),'OR':([5,20,25,26,27,28,29,40,41,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,106,108,113,118,],[-29,55,-67,-63,-64,-65,-66,55,-67,55,55,55,55,55,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,55,-68,55,55,55,55,]),'NE':([5,20,25,26,27,28,29,40,41,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,106,108,113,118,],[-29,56,-67,-63,-64,-65,-66,56,-67,56,56,56,56,56,-50,-51,-52,-53,56,56,-56,-57,56,56,-60,56,-62,56,-68,56,56,56,56,]),'EQ':([5,20,25,26,27,28,29,40,41,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,106,108,113,118,],[-29,57,-67,-63,-64,-65,-66,57,-67,57,57,57,57,57,-50,-51,-52,-53,57,57,57,-57,57,57,-60,57,-62,57,-68,57,57,57,57,]),'LT':([5,20,25,26,27,28,29,40,41,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,106,108,113,118,],[-29,58,-67,-63,-64,-65,-66,58,-67,58,58,58,58,58,-50,-51,-52,-53,58,58,-56,-57,-58,-59,-60,-61,-62,58,-68,58,58,58,58,]),'GT':([5,20,25,26,27,28,29,40,41,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,106,108,113,118,],[-29,59,-67,-63,-64,-65,-66,59,-67,59,59,59,59,59,-50,-51,-52,-53,59,59,-56,-57,59,-59,-60,-61,-62,59,-68,59,59,59,59,]),'LE':([5,20,25,26,27,28,29,40,41,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,106,108,113,118,],[-29,60,-67,-63,-64,-65,-66,60,-67,60,60,60,60,60,-50,-51,-52,-53,60,60,60,60,60,60,-60,60,-62,60,-68,60,60,60,60,]),'GE':([5,20,25,26,27,28,29,40,41,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,106,108,113,118,],[-29,61,-67,-63,-64,-65,-66,61,-67,61,61,61,61,61,-50,-51,-52,-53,61,61,-56,-57,61,61,-60,-61,-62,61,-68,61,61,61,61,]),'END':([5,10,14,20,25,26,27,28,29,37,38,41,49,72,78,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,102,103,104,109,130,131,139,141,146,],[-29,-26,-31,-49,-67,-63,-64,-65,-66,72,-27,-67,-48,-25,109,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-30,-68,-28,-32,-36,-42,-38,-39,-33,-44,-45,]),'THEN':([5,26,27,28,29,39,40,41,81,82,83,84,85,86,87,88,89,90,91,92,97,100,],[-29,-63,-64,-65,-66,74,-34,-67,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-68,]),'DO':([5,26,27,28,29,41,42,43,81,82,83,84,85,86,87,88,89,90,91,92,97,100,105,106,107,108,],[-29,-63,-64,-65,-66,-67,75,-37,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-68,120,-40,121,-41,]),'ELSE':([5,10,14,20,25,26,27,28,29,41,49,72,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,103,104,109,130,131,139,],[-29,-26,-31,-49,-67,-63,-64,-65,-66,-67,-48,-25,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-30,-68,119,-36,-42,-38,-39,-33,]),'CLOSE_PAREN':([5,26,27,28,29,41,66,69,70,81,82,83,84,85,86,87,88,89,90,91,92,97,100,114,115,117,118,126,127,136,144,],[-29,-63,-64,-65,-66,-67,97,100,-69,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-68,124,-20,128,-70,-22,-23,-21,-24,]),'SEPARATOR':([5,26,27,28,29,41,62,63,64,69,70,81,82,83,84,85,86,87,88,89,90,91,92,97,100,112,113,118,126,127,144,],[-29,-63,-64,-65,-66,-67,94,-13,-11,101,-69,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-68,-14,-12,-70,137,-23,-24,]),'TO':([5,26,27,28,29,41,44,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,],[-29,-63,-64,-65,-66,-67,76,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-30,-68,]),'DOWNTO':([5,26,27,28,29,41,44,81,82,83,84,85,86,87,88,89,90,91,92,97,99,100,],[-29,-63,-64,-65,-66,-67,77,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-30,-68,]),'COLON':([79,80,110,128,],[111,-47,122,138,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declist':([4,124,145,],[6,134,148,]),'block':([4,6,74,75,120,121,123,124,129,132,134,145,148,],[7,34,103,104,130,131,133,135,139,140,142,149,150,]),'dec':([4,6,124,134,145,148,],[8,35,8,35,8,35,]),'stmt':([4,6,9,73,74,75,120,121,123,124,129,132,134,145,148,],[10,10,38,102,10,10,10,10,10,10,10,10,10,10,10,]),'vardec':([4,6,124,134,145,148,],[11,11,11,11,11,11,]),'procdec':([4,6,124,134,145,148,],[12,12,12,12,12,12,]),'funcdec':([4,6,124,134,145,148,],[13,13,13,13,13,13,]),'assignstmt':([4,6,9,17,73,74,75,120,121,123,124,129,132,134,145,148,],[14,14,14,44,14,14,14,14,14,14,14,14,14,14,14,14,]),'exp':([4,6,9,15,16,18,19,23,33,50,51,52,53,54,55,56,57,58,59,60,61,68,73,74,75,76,77,95,101,120,121,123,124,129,132,134,145,148,],[20,20,20,40,43,48,49,66,70,81,82,83,84,85,86,87,88,89,90,91,92,99,20,20,20,106,108,113,118,20,20,20,20,20,20,20,20,20,]),'type':([4,6,96,98,124,125,134,138,145,148,],[21,21,116,116,21,116,21,145,21,21,]),'lvalue':([4,6,9,15,16,17,18,19,23,33,50,51,52,53,54,55,56,57,58,59,60,61,68,73,74,75,76,77,95,101,120,121,123,124,129,132,134,145,148,],[25,25,25,41,41,45,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,25,25,25,41,41,41,41,25,25,25,25,25,25,25,25,25,]),'stmtlist':([9,],[37,]),'controlifexp':([15,],[39,]),'controlwhileexp':([16,],[42,]),'controlcaseexp':([18,],[47,]),'idlist':([21,],[62,]),'iddec':([21,94,],[63,112,]),'explist':([33,],[69,]),'caseelement':([47,],[78,]),'case':([47,78,],[79,110,]),'controlforupexp':([76,],[105,]),'controlfordownexp':([77,],[107,]),'paramdecs':([96,98,],[114,117,]),'paramdec':([96,98,125,],[115,115,136,]),'caseelementcontrol':([111,122,],[123,132,]),'paramlist':([116,],[126,]),'controlelse':([119,],[129,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMI_COLON declist block SEMI_COLON','program',6,'p_prog_declist','parser.py',35),
  ('program -> PROGRAM ID SEMI_COLON block SEMI_COLON','program',5,'p_prog_block','parser.py',40),
  ('declist -> dec','declist',1,'p_declist','parser.py',45),
  ('declist -> declist dec','declist',2,'p_declist_ext','parser.py',49),
  ('dec -> vardec','dec',1,'p_dec_vardec','parser.py',53),
  ('dec -> procdec','dec',1,'p_dec_procdec','parser.py',57),
  ('dec -> funcdec','dec',1,'p_dec_funcdec','parser.py',61),
  ('type -> INT','type',1,'p_type_int','parser.py',65),
  ('type -> REAL','type',1,'p_type_real','parser.py',69),
  ('type -> BOOL','type',1,'p_type_bool','parser.py',73),
  ('iddec -> ID','iddec',1,'p_iddec_id','parser.py',77),
  ('iddec -> ID ASSIGN exp','iddec',3,'p_iddec_exp','parser.py',81),
  ('idlist -> iddec','idlist',1,'p_idlist_iddec','parser.py',89),
  ('idlist -> idlist SEPARATOR iddec','idlist',3,'p_idlist_ext','parser.py',93),
  ('vardec -> type idlist SEMI_COLON','vardec',3,'p_vardec','parser.py',97),
  ('procdec -> PROCEDURE ID OPEN_PAREN paramdecs CLOSE_PAREN declist block SEMI_COLON','procdec',8,'p_procdec_declist','parser.py',101),
  ('procdec -> PROCEDURE ID OPEN_PAREN paramdecs CLOSE_PAREN block SEMI_COLON','procdec',7,'p_procdec_block','parser.py',105),
  ('funcdec -> FUNCTION ID OPEN_PAREN paramdecs CLOSE_PAREN COLON type declist block SEMI_COLON','funcdec',10,'p_funcdec_declist','parser.py',109),
  ('funcdec -> FUNCTION ID OPEN_PAREN paramdecs CLOSE_PAREN COLON type block SEMI_COLON','funcdec',9,'p_funcdec_block','parser.py',113),
  ('paramdecs -> paramdec','paramdecs',1,'p_paramdecs','parser.py',117),
  ('paramdecs -> paramdecs SEMI_COLON paramdec','paramdecs',3,'p_paramdecs_ext','parser.py',121),
  ('paramdec -> type paramlist','paramdec',2,'p_paramdec','parser.py',125),
  ('paramlist -> ID','paramlist',1,'p_paramlist','parser.py',129),
  ('paramlist -> paramlist SEPARATOR ID','paramlist',3,'p_paramlist_ext','parser.py',133),
  ('block -> BEGIN stmtlist END','block',3,'p_block_stmtlist','parser.py',137),
  ('block -> stmt','block',1,'p_block_stmt','parser.py',141),
  ('stmtlist -> stmt','stmtlist',1,'p_stmtlist','parser.py',145),
  ('stmtlist -> stmtlist SEMI_COLON stmt','stmtlist',3,'p_stmtlist_ext','parser.py',149),
  ('lvalue -> ID','lvalue',1,'p_lvalue','parser.py',153),
  ('assignstmt -> lvalue ASSIGN exp','assignstmt',3,'p_stmt_assign','parser.py',158),
  ('stmt -> assignstmt','stmt',1,'p_assign_stmt_assign','parser.py',167),
  ('stmt -> IF controlifexp THEN block','stmt',4,'p_stmt_if','parser.py',171),
  ('stmt -> IF controlifexp THEN block ELSE controlelse block','stmt',7,'p_stmt_if_else','parser.py',176),
  ('controlifexp -> exp','controlifexp',1,'p_control_if_exp','parser.py',180),
  ('controlelse -> <empty>','controlelse',0,'p_controlelse','parser.py',187),
  ('stmt -> WHILE controlwhileexp DO block','stmt',4,'p_stmt_while','parser.py',191),
  ('controlwhileexp -> exp','controlwhileexp',1,'p_control_while_exp','parser.py',197),
  ('stmt -> FOR assignstmt TO controlforupexp DO block','stmt',6,'p_stmt_for_up','parser.py',204),
  ('stmt -> FOR assignstmt DOWNTO controlfordownexp DO block','stmt',6,'p_stmt_for_down','parser.py',215),
  ('controlforupexp -> exp','controlforupexp',1,'p_control_for_up_exp','parser.py',226),
  ('controlfordownexp -> exp','controlfordownexp',1,'p_control_for_down_exp','parser.py',232),
  ('stmt -> CASE controlcaseexp caseelement END','stmt',4,'p_stmt_case','parser.py',238),
  ('controlcaseexp -> exp','controlcaseexp',1,'p_control_case_exp','parser.py',244),
  ('caseelement -> case COLON caseelementcontrol block SEMI_COLON','caseelement',5,'p_caseelement','parser.py',256),
  ('caseelement -> caseelement case COLON caseelementcontrol block SEMI_COLON','caseelement',6,'p_caseelement_ext','parser.py',262),
  ('caseelementcontrol -> <empty>','caseelementcontrol',0,'p_case_element_control','parser.py',269),
  ('case -> INTEGER','case',1,'p_case_integer','parser.py',277),
  ('stmt -> RETURN exp','stmt',2,'p_stmt_return','parser.py',282),
  ('stmt -> exp','stmt',1,'p_stmt_exp','parser.py',286),
  ('exp -> exp SUM exp','exp',3,'p_exp_sum','parser.py',290),
  ('exp -> exp SUB exp','exp',3,'p_exp_sub','parser.py',296),
  ('exp -> exp MUL exp','exp',3,'p_exp_mul','parser.py',302),
  ('exp -> exp DIV exp','exp',3,'p_exp_div','parser.py',308),
  ('exp -> exp AND exp','exp',3,'p_exp_and','parser.py',314),
  ('exp -> exp OR exp','exp',3,'p_exp_or','parser.py',325),
  ('exp -> exp NE exp','exp',3,'p_exp_ne','parser.py',336),
  ('exp -> exp EQ exp','exp',3,'p_exp_eq','parser.py',342),
  ('exp -> exp LT exp','exp',3,'p_exp_lt','parser.py',348),
  ('exp -> exp GT exp','exp',3,'p_exp_gt','parser.py',354),
  ('exp -> exp LE exp','exp',3,'p_exp_le','parser.py',360),
  ('exp -> exp GE exp','exp',3,'p_exp_ge','parser.py',366),
  ('exp -> OPEN_PAREN exp CLOSE_PAREN','exp',3,'p_exp_paren','parser.py',372),
  ('exp -> REALNUMBER','exp',1,'p_exp_real','parser.py',378),
  ('exp -> INTEGER','exp',1,'p_exp_integer','parser.py',383),
  ('exp -> TRUE','exp',1,'p_exp_true','parser.py',387),
  ('exp -> FALSE','exp',1,'p_exp_false','parser.py',391),
  ('exp -> lvalue','exp',1,'p_exp_lvalue','parser.py',395),
  ('exp -> ID OPEN_PAREN explist CLOSE_PAREN','exp',4,'p_exp_func','parser.py',399),
  ('explist -> exp','explist',1,'p_explist','parser.py',403),
  ('explist -> explist SEPARATOR exp','explist',3,'p_explist_ext','parser.py',407),
]
