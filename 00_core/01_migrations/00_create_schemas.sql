BEGIN;

-- Criar schemas
CREATE SCHEMA IF NOT EXISTS notes;
CREATE SCHEMA IF NOT EXISTS users;
CREATE SCHEMA IF NOT EXISTS ai;
CREATE SCHEMA IF NOT EXISTS tasks;

-- Configurar permissões
GRANT USAGE ON SCHEMA notes TO authenticated;
GRANT USAGE ON SCHEMA users TO authenticated;
GRANT USAGE ON SCHEMA ai TO authenticated;
GRANT USAGE ON SCHEMA tasks TO authenticated;

COMMIT;