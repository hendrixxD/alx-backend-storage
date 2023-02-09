-- A trigger is a named database object that is associated with a table, and it activates when a particular event (e.g. an insert, update or delete) occurs for the table. The statement CREATE TRIGGER creates a new trigger in MySQL. 

-- SYntax:

CREATE     
DEFINER = { user | CURRENT_USER }]     
TRIGGER trigger_name     
trigger_time trigger_event     
ON tbl_name FOR EACH ROW     
trigger_body
trigger_time: { BEFORE | AFTER } 
trigger_event: { INSERT | UPDATE | DELETE }
