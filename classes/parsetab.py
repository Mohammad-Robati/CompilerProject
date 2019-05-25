
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftTHENleftELSEleftORleftANDleftLTleftGTleftGEleftNEleftEQleftLEleftSUMSUBleftMULDIVAND ASSIGN BEGIN BOOL CASE CLOSE_PAREN COLON DIV DO DOWNTO ELSE END EQ FALSE FOR FUNCTION GE GT ID IF INT INTEGER LE LT MUL NE OPEN_PAREN OR PROCEDURE PROGRAM REAL REALNUMBER RETURN SEMI_COLON SEPARATOR SUB SUM THEN TO TRUE WHILEprogram : PROGRAM ID SEMI_COLON declistlast block SEMI_COLONdeclistlast : declistdeclistlast : declist : decdeclist : declist decdec : vardecdec : procdecdec : funcdectype : INTtype : REALtype : BOOLiddec : IDiddec : ID ASSIGN expidlist : iddecidlist : idlist SEPARATOR iddecvardec : type idlist SEMI_COLONparamdecslast : paramdecsparamdecslast : procdec : PROCEDURE ID OPEN_PAREN paramdecslast CLOSE_PAREN declistlast block SEMI_COLONfuncdec : FUNCTION ID OPEN_PAREN paramdecslast CLOSE_PAREN COLON type declistlast block SEMI_COLONparamdecs : paramdecparamdecs : paramdecs SEMI_COLON paramdecparamdec : type paramlistparamlist : IDparamlist : paramlist SEPARATOR IDblock : BEGIN stmtlist ENDblock : stmtstmtlist : stmtstmtlist : stmtlist SEMI_COLON stmtlvalue : IDassignstmt : lvalue ASSIGN expstmt : assignstmtstmt : IF controlifexp THEN blockstmt : IF controlifexp THEN block ELSE controlelse blockcontrolifexp : expcontrolelse : stmt : WHILE controlwhileexp DO blockcontrolwhileexp : expstmt : FOR assignstmt TO controlforupexp DO blockstmt : FOR assignstmt DOWNTO controlfordownexp DO blockcontrolforupexp : expcontrolfordownexp : expstmt : CASE controlcaseexp caseelement ENDcontrolcaseexp : exp caseelement : case COLON caseelementcontrol block SEMI_COLON caseelement : caseelement case COLON caseelementcontrol block SEMI_COLONcaseelementcontrol : case : INTEGERstmt : RETURN expstmt : expexp : exp SUM expexp : exp SUB expexp : exp MUL expexp : exp DIV expexp : exp AND expexp : exp OR expexp : exp NE expexp : exp EQ expexp : exp LT expexp : exp GT expexp : exp LE expexp : exp GE expexp : OPEN_PAREN exp CLOSE_PARENexp : REALNUMBERexp : INTEGERexp : TRUEexp : FALSEexp : lvalueexp : ID OPEN_PAREN explist CLOSE_PARENexplist : expexplist : explist SEPARATOR exp'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,41,],[0,-1,]),'ID':([2,4,5,6,7,8,9,10,11,12,13,14,15,16,19,22,23,24,25,26,29,34,40,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,77,78,79,80,81,104,107,117,118,124,125,126,127,128,129,131,133,136,140,144,145,148,],[3,-3,17,-2,-4,-6,-7,-8,37,38,39,-9,-10,-11,17,17,17,51,17,17,17,-5,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-16,37,17,17,17,17,17,17,121,17,-47,-3,-36,17,17,-47,17,17,139,17,17,-3,-19,17,-20,]),'SEMI_COLON':([3,17,18,20,21,27,28,30,31,32,33,35,36,37,42,43,46,54,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,106,108,109,110,115,120,121,130,134,135,137,138,139,141,142,147,],[4,-30,41,-27,-32,-50,-68,-64,-65,-66,-67,69,-14,-12,77,-28,-68,-49,-26,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-31,-63,-15,-13,119,-21,-69,-29,-33,-37,-43,-23,-24,-22,-39,-40,143,144,-25,-34,146,148,]),'BEGIN':([4,5,6,7,8,9,10,14,15,16,34,69,78,79,117,118,124,125,126,127,128,129,133,136,140,144,145,148,],[-3,19,-2,-4,-6,-7,-8,-9,-10,-11,-5,-16,19,19,-47,-3,-36,19,19,-47,19,19,19,19,-3,-19,19,-20,]),'IF':([4,5,6,7,8,9,10,14,15,16,19,34,69,77,78,79,117,118,124,125,126,127,128,129,133,136,140,144,145,148,],[-3,22,-2,-4,-6,-7,-8,-9,-10,-11,22,-5,-16,22,22,22,-47,-3,-36,22,22,-47,22,22,22,22,-3,-19,22,-20,]),'WHILE':([4,5,6,7,8,9,10,14,15,16,19,34,69,77,78,79,117,118,124,125,126,127,128,129,133,136,140,144,145,148,],[-3,23,-2,-4,-6,-7,-8,-9,-10,-11,23,-5,-16,23,23,23,-47,-3,-36,23,23,-47,23,23,23,23,-3,-19,23,-20,]),'FOR':([4,5,6,7,8,9,10,14,15,16,19,34,69,77,78,79,117,118,124,125,126,127,128,129,133,136,140,144,145,148,],[-3,24,-2,-4,-6,-7,-8,-9,-10,-11,24,-5,-16,24,24,24,-47,-3,-36,24,24,-47,24,24,24,24,-3,-19,24,-20,]),'CASE':([4,5,6,7,8,9,10,14,15,16,19,34,69,77,78,79,117,118,124,125,126,127,128,129,133,136,140,144,145,148,],[-3,25,-2,-4,-6,-7,-8,-9,-10,-11,25,-5,-16,25,25,25,-47,-3,-36,25,25,-47,25,25,25,25,-3,-19,25,-20,]),'RETURN':([4,5,6,7,8,9,10,14,15,16,19,34,69,77,78,79,117,118,124,125,126,127,128,129,133,136,140,144,145,148,],[-3,26,-2,-4,-6,-7,-8,-9,-10,-11,26,-5,-16,26,26,26,-47,-3,-36,26,26,-47,26,26,26,26,-3,-19,26,-20,]),'OPEN_PAREN':([4,5,6,7,8,9,10,14,15,16,17,19,22,23,25,26,29,34,38,39,40,55,56,57,58,59,60,61,62,63,64,65,66,67,69,71,77,78,79,80,81,107,117,118,124,125,126,127,128,129,133,136,140,144,145,148,],[-3,29,-2,-4,-6,-7,-8,-9,-10,-11,40,29,29,29,29,29,29,-5,72,73,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-16,29,29,29,29,29,29,29,-47,-3,-36,29,29,-47,29,29,29,29,-3,-19,29,-20,]),'REALNUMBER':([4,5,6,7,8,9,10,14,15,16,19,22,23,25,26,29,34,40,55,56,57,58,59,60,61,62,63,64,65,66,67,69,71,77,78,79,80,81,107,117,118,124,125,126,127,128,129,133,136,140,144,145,148,],[-3,30,-2,-4,-6,-7,-8,-9,-10,-11,30,30,30,30,30,30,-5,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-16,30,30,30,30,30,30,30,-47,-3,-36,30,30,-47,30,30,30,30,-3,-19,30,-20,]),'INTEGER':([4,5,6,7,8,9,10,14,15,16,17,19,22,23,25,26,29,30,31,32,33,34,40,46,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,69,71,77,78,79,80,81,82,85,86,87,88,89,90,91,92,93,94,95,96,98,106,107,117,118,124,125,126,127,128,129,133,136,140,143,144,145,146,148,],[-3,31,-2,-4,-6,-7,-8,-9,-10,-11,-30,31,31,31,31,31,31,-64,-65,-66,-67,-5,31,-68,84,-44,31,31,31,31,31,31,31,31,31,31,31,31,31,-16,31,31,31,31,31,31,84,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-69,31,-47,-3,-36,31,31,-47,31,31,31,31,-3,-45,-19,31,-46,-20,]),'TRUE':([4,5,6,7,8,9,10,14,15,16,19,22,23,25,26,29,34,40,55,56,57,58,59,60,61,62,63,64,65,66,67,69,71,77,78,79,80,81,107,117,118,124,125,126,127,128,129,133,136,140,144,145,148,],[-3,32,-2,-4,-6,-7,-8,-9,-10,-11,32,32,32,32,32,32,-5,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-16,32,32,32,32,32,32,32,-47,-3,-36,32,32,-47,32,32,32,32,-3,-19,32,-20,]),'FALSE':([4,5,6,7,8,9,10,14,15,16,19,22,23,25,26,29,34,40,55,56,57,58,59,60,61,62,63,64,65,66,67,69,71,77,78,79,80,81,107,117,118,124,125,126,127,128,129,133,136,140,144,145,148,],[-3,33,-2,-4,-6,-7,-8,-9,-10,-11,33,33,33,33,33,33,-5,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-16,33,33,33,33,33,33,33,-47,-3,-36,33,33,-47,33,33,33,33,-3,-19,33,-20,]),'PROCEDURE':([4,6,7,8,9,10,14,15,16,34,69,118,140,144,148,],[12,12,-4,-6,-7,-8,-9,-10,-11,-5,-16,12,12,-19,-20,]),'FUNCTION':([4,6,7,8,9,10,14,15,16,34,69,118,140,144,148,],[13,13,-4,-6,-7,-8,-9,-10,-11,-5,-16,13,13,-19,-20,]),'INT':([4,6,7,8,9,10,14,15,16,34,69,72,73,118,119,132,140,144,148,],[14,14,-4,-6,-7,-8,-9,-10,-11,-5,-16,14,14,14,14,14,14,-19,-20,]),'REAL':([4,6,7,8,9,10,14,15,16,34,69,72,73,118,119,132,140,144,148,],[15,15,-4,-6,-7,-8,-9,-10,-11,-5,-16,15,15,15,15,15,15,-19,-20,]),'BOOL':([4,6,7,8,9,10,14,15,16,34,69,72,73,118,119,132,140,144,148,],[16,16,-4,-6,-7,-8,-9,-10,-11,-5,-16,16,16,16,16,16,16,-19,-20,]),'ASSIGN':([17,28,37,50,51,],[-30,67,71,67,-30,]),'SUM':([17,27,28,30,31,32,33,45,46,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,106,112,114,123,],[-30,55,-68,-64,-65,-66,-67,55,-68,55,55,55,55,55,-51,-52,-53,-54,55,55,55,55,55,55,55,55,55,-63,55,-69,55,55,55,]),'SUB':([17,27,28,30,31,32,33,45,46,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,106,112,114,123,],[-30,56,-68,-64,-65,-66,-67,56,-68,56,56,56,56,56,-51,-52,-53,-54,56,56,56,56,56,56,56,56,56,-63,56,-69,56,56,56,]),'MUL':([17,27,28,30,31,32,33,45,46,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,106,112,114,123,],[-30,57,-68,-64,-65,-66,-67,57,-68,57,57,57,57,57,57,57,-53,-54,57,57,57,57,57,57,57,57,57,-63,57,-69,57,57,57,]),'DIV':([17,27,28,30,31,32,33,45,46,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,106,112,114,123,],[-30,58,-68,-64,-65,-66,-67,58,-68,58,58,58,58,58,58,58,-53,-54,58,58,58,58,58,58,58,58,58,-63,58,-69,58,58,58,]),'AND':([17,27,28,30,31,32,33,45,46,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,106,112,114,123,],[-30,59,-68,-64,-65,-66,-67,59,-68,59,59,59,59,59,-51,-52,-53,-54,-55,59,-57,-58,-59,-60,-61,-62,59,-63,59,-69,59,59,59,]),'OR':([17,27,28,30,31,32,33,45,46,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,106,112,114,123,],[-30,60,-68,-64,-65,-66,-67,60,-68,60,60,60,60,60,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,60,-63,60,-69,60,60,60,]),'NE':([17,27,28,30,31,32,33,45,46,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,106,112,114,123,],[-30,61,-68,-64,-65,-66,-67,61,-68,61,61,61,61,61,-51,-52,-53,-54,61,61,-57,-58,61,61,-61,61,61,-63,61,-69,61,61,61,]),'EQ':([17,27,28,30,31,32,33,45,46,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,106,112,114,123,],[-30,62,-68,-64,-65,-66,-67,62,-68,62,62,62,62,62,-51,-52,-53,-54,62,62,62,-58,62,62,-61,62,62,-63,62,-69,62,62,62,]),'LT':([17,27,28,30,31,32,33,45,46,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,106,112,114,123,],[-30,63,-68,-64,-65,-66,-67,63,-68,63,63,63,63,63,-51,-52,-53,-54,63,63,-57,-58,-59,-60,-61,-62,63,-63,63,-69,63,63,63,]),'GT':([17,27,28,30,31,32,33,45,46,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,106,112,114,123,],[-30,64,-68,-64,-65,-66,-67,64,-68,64,64,64,64,64,-51,-52,-53,-54,64,64,-57,-58,64,-60,-61,-62,64,-63,64,-69,64,64,64,]),'LE':([17,27,28,30,31,32,33,45,46,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,106,112,114,123,],[-30,65,-68,-64,-65,-66,-67,65,-68,65,65,65,65,65,-51,-52,-53,-54,65,65,65,65,65,65,-61,65,65,-63,65,-69,65,65,65,]),'GE':([17,27,28,30,31,32,33,45,46,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,106,112,114,123,],[-30,66,-68,-64,-65,-66,-67,66,-68,66,66,66,66,66,-51,-52,-53,-54,66,66,-57,-58,66,66,-61,-62,66,-63,66,-69,66,66,66,]),'END':([17,20,21,27,28,30,31,32,33,42,43,46,54,76,82,85,86,87,88,89,90,91,92,93,94,95,96,97,98,106,108,109,110,115,134,135,141,143,146,],[-30,-27,-32,-50,-68,-64,-65,-66,-67,76,-28,-68,-49,-26,115,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-31,-63,-69,-29,-33,-37,-43,-39,-40,-34,-45,-46,]),'THEN':([17,30,31,32,33,44,45,46,85,86,87,88,89,90,91,92,93,94,95,96,98,106,],[-30,-64,-65,-66,-67,78,-35,-68,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-69,]),'DO':([17,30,31,32,33,46,47,48,85,86,87,88,89,90,91,92,93,94,95,96,98,106,111,112,113,114,],[-30,-64,-65,-66,-67,-68,79,-38,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-69,125,-41,126,-42,]),'ELSE':([17,20,21,27,28,30,31,32,33,46,54,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,106,109,110,115,134,135,141,],[-30,-27,-32,-50,-68,-64,-65,-66,-67,-68,-49,-26,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-31,-63,-69,124,-37,-43,-39,-40,-34,]),'CLOSE_PAREN':([17,30,31,32,33,46,68,72,73,74,75,85,86,87,88,89,90,91,92,93,94,95,96,98,101,102,103,105,106,120,121,123,130,139,],[-30,-64,-65,-66,-67,-68,98,-18,-18,106,-70,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,118,-17,-21,122,-69,-23,-24,-71,-22,-25,]),'SEPARATOR':([17,30,31,32,33,35,36,37,46,74,75,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,106,120,121,123,139,],[-30,-64,-65,-66,-67,70,-14,-12,-68,107,-70,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,-15,-13,-69,131,-24,-71,-25,]),'TO':([17,30,31,32,33,46,49,85,86,87,88,89,90,91,92,93,94,95,96,97,98,106,],[-30,-64,-65,-66,-67,-68,80,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-31,-63,-69,]),'DOWNTO':([17,30,31,32,33,46,49,85,86,87,88,89,90,91,92,93,94,95,96,97,98,106,],[-30,-64,-65,-66,-67,-68,81,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-62,-31,-63,-69,]),'COLON':([83,84,116,122,],[117,-48,127,132,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declistlast':([4,118,140,],[5,129,145,]),'declist':([4,118,140,],[6,6,6,]),'dec':([4,6,118,140,],[7,34,7,7,]),'vardec':([4,6,118,140,],[8,8,8,8,]),'procdec':([4,6,118,140,],[9,9,9,9,]),'funcdec':([4,6,118,140,],[10,10,10,10,]),'type':([4,6,72,73,118,119,132,140,],[11,11,104,104,11,104,140,11,]),'block':([5,78,79,125,126,128,129,133,136,145,],[18,109,110,134,135,137,138,141,142,147,]),'stmt':([5,19,77,78,79,125,126,128,129,133,136,145,],[20,43,108,20,20,20,20,20,20,20,20,20,]),'assignstmt':([5,19,24,77,78,79,125,126,128,129,133,136,145,],[21,21,49,21,21,21,21,21,21,21,21,21,21,]),'exp':([5,19,22,23,25,26,29,40,55,56,57,58,59,60,61,62,63,64,65,66,67,71,77,78,79,80,81,107,125,126,128,129,133,136,145,],[27,27,45,48,53,54,68,75,85,86,87,88,89,90,91,92,93,94,95,96,97,100,27,27,27,112,114,123,27,27,27,27,27,27,27,]),'lvalue':([5,19,22,23,24,25,26,29,40,55,56,57,58,59,60,61,62,63,64,65,66,67,71,77,78,79,80,81,107,125,126,128,129,133,136,145,],[28,28,46,46,50,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,28,28,28,46,46,46,28,28,28,28,28,28,28,]),'idlist':([11,],[35,]),'iddec':([11,70,],[36,99,]),'stmtlist':([19,],[42,]),'controlifexp':([22,],[44,]),'controlwhileexp':([23,],[47,]),'controlcaseexp':([25,],[52,]),'explist':([40,],[74,]),'caseelement':([52,],[82,]),'case':([52,82,],[83,116,]),'paramdecslast':([72,73,],[101,105,]),'paramdecs':([72,73,],[102,102,]),'paramdec':([72,73,119,],[103,103,130,]),'controlforupexp':([80,],[111,]),'controlfordownexp':([81,],[113,]),'paramlist':([104,],[120,]),'caseelementcontrol':([117,127,],[128,136,]),'controlelse':([124,],[133,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMI_COLON declistlast block SEMI_COLON','program',6,'p_prog_declist','parser.py',39),
  ('declistlast -> declist','declistlast',1,'p_declist_last','parser.py',44),
  ('declistlast -> <empty>','declistlast',0,'p_declist_empty','parser.py',49),
  ('declist -> dec','declist',1,'p_declist','parser.py',54),
  ('declist -> declist dec','declist',2,'p_declist_ext','parser.py',60),
  ('dec -> vardec','dec',1,'p_dec_vardec','parser.py',66),
  ('dec -> procdec','dec',1,'p_dec_procdec','parser.py',72),
  ('dec -> funcdec','dec',1,'p_dec_funcdec','parser.py',76),
  ('type -> INT','type',1,'p_type_int','parser.py',81),
  ('type -> REAL','type',1,'p_type_real','parser.py',85),
  ('type -> BOOL','type',1,'p_type_bool','parser.py',89),
  ('iddec -> ID','iddec',1,'p_iddec_id','parser.py',93),
  ('iddec -> ID ASSIGN exp','iddec',3,'p_iddec_exp','parser.py',100),
  ('idlist -> iddec','idlist',1,'p_idlist_iddec','parser.py',112),
  ('idlist -> idlist SEPARATOR iddec','idlist',3,'p_idlist_ext','parser.py',118),
  ('vardec -> type idlist SEMI_COLON','vardec',3,'p_vardec','parser.py',124),
  ('paramdecslast -> paramdecs','paramdecslast',1,'p_paramdecs_last','parser.py',129),
  ('paramdecslast -> <empty>','paramdecslast',0,'p_paramdecs_empty','parser.py',133),
  ('procdec -> PROCEDURE ID OPEN_PAREN paramdecslast CLOSE_PAREN declistlast block SEMI_COLON','procdec',8,'p_procdec_declist','parser.py',138),
  ('funcdec -> FUNCTION ID OPEN_PAREN paramdecslast CLOSE_PAREN COLON type declistlast block SEMI_COLON','funcdec',10,'p_funcdec_declist','parser.py',142),
  ('paramdecs -> paramdec','paramdecs',1,'p_paramdecs','parser.py',146),
  ('paramdecs -> paramdecs SEMI_COLON paramdec','paramdecs',3,'p_paramdecs_ext','parser.py',150),
  ('paramdec -> type paramlist','paramdec',2,'p_paramdec','parser.py',154),
  ('paramlist -> ID','paramlist',1,'p_paramlist','parser.py',158),
  ('paramlist -> paramlist SEPARATOR ID','paramlist',3,'p_paramlist_ext','parser.py',162),
  ('block -> BEGIN stmtlist END','block',3,'p_block_stmtlist','parser.py',166),
  ('block -> stmt','block',1,'p_block_stmt','parser.py',170),
  ('stmtlist -> stmt','stmtlist',1,'p_stmtlist','parser.py',174),
  ('stmtlist -> stmtlist SEMI_COLON stmt','stmtlist',3,'p_stmtlist_ext','parser.py',178),
  ('lvalue -> ID','lvalue',1,'p_lvalue','parser.py',182),
  ('assignstmt -> lvalue ASSIGN exp','assignstmt',3,'p_stmt_assign','parser.py',189),
  ('stmt -> assignstmt','stmt',1,'p_assign_stmt_assign','parser.py',198),
  ('stmt -> IF controlifexp THEN block','stmt',4,'p_stmt_if','parser.py',202),
  ('stmt -> IF controlifexp THEN block ELSE controlelse block','stmt',7,'p_stmt_if_else','parser.py',207),
  ('controlifexp -> exp','controlifexp',1,'p_control_if_exp','parser.py',211),
  ('controlelse -> <empty>','controlelse',0,'p_controlelse','parser.py',218),
  ('stmt -> WHILE controlwhileexp DO block','stmt',4,'p_stmt_while','parser.py',222),
  ('controlwhileexp -> exp','controlwhileexp',1,'p_control_while_exp','parser.py',228),
  ('stmt -> FOR assignstmt TO controlforupexp DO block','stmt',6,'p_stmt_for_up','parser.py',235),
  ('stmt -> FOR assignstmt DOWNTO controlfordownexp DO block','stmt',6,'p_stmt_for_down','parser.py',246),
  ('controlforupexp -> exp','controlforupexp',1,'p_control_for_up_exp','parser.py',257),
  ('controlfordownexp -> exp','controlfordownexp',1,'p_control_for_down_exp','parser.py',263),
  ('stmt -> CASE controlcaseexp caseelement END','stmt',4,'p_stmt_case','parser.py',269),
  ('controlcaseexp -> exp','controlcaseexp',1,'p_control_case_exp','parser.py',275),
  ('caseelement -> case COLON caseelementcontrol block SEMI_COLON','caseelement',5,'p_caseelement','parser.py',287),
  ('caseelement -> caseelement case COLON caseelementcontrol block SEMI_COLON','caseelement',6,'p_caseelement_ext','parser.py',293),
  ('caseelementcontrol -> <empty>','caseelementcontrol',0,'p_case_element_control','parser.py',300),
  ('case -> INTEGER','case',1,'p_case_integer','parser.py',308),
  ('stmt -> RETURN exp','stmt',2,'p_stmt_return','parser.py',313),
  ('stmt -> exp','stmt',1,'p_stmt_exp','parser.py',317),
  ('exp -> exp SUM exp','exp',3,'p_exp_sum','parser.py',321),
  ('exp -> exp SUB exp','exp',3,'p_exp_sub','parser.py',327),
  ('exp -> exp MUL exp','exp',3,'p_exp_mul','parser.py',333),
  ('exp -> exp DIV exp','exp',3,'p_exp_div','parser.py',339),
  ('exp -> exp AND exp','exp',3,'p_exp_and','parser.py',345),
  ('exp -> exp OR exp','exp',3,'p_exp_or','parser.py',356),
  ('exp -> exp NE exp','exp',3,'p_exp_ne','parser.py',367),
  ('exp -> exp EQ exp','exp',3,'p_exp_eq','parser.py',373),
  ('exp -> exp LT exp','exp',3,'p_exp_lt','parser.py',379),
  ('exp -> exp GT exp','exp',3,'p_exp_gt','parser.py',385),
  ('exp -> exp LE exp','exp',3,'p_exp_le','parser.py',391),
  ('exp -> exp GE exp','exp',3,'p_exp_ge','parser.py',397),
  ('exp -> OPEN_PAREN exp CLOSE_PAREN','exp',3,'p_exp_paren','parser.py',403),
  ('exp -> REALNUMBER','exp',1,'p_exp_real','parser.py',409),
  ('exp -> INTEGER','exp',1,'p_exp_integer','parser.py',414),
  ('exp -> TRUE','exp',1,'p_exp_true','parser.py',418),
  ('exp -> FALSE','exp',1,'p_exp_false','parser.py',424),
  ('exp -> lvalue','exp',1,'p_exp_lvalue','parser.py',430),
  ('exp -> ID OPEN_PAREN explist CLOSE_PAREN','exp',4,'p_exp_func','parser.py',438),
  ('explist -> exp','explist',1,'p_explist','parser.py',448),
  ('explist -> explist SEPARATOR exp','explist',3,'p_explist_ext','parser.py',454),
]
