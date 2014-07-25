create table michishiki (
  id integer primary key autoincrement,
  latitude real,
  longitude real,
  posted_by text,
  title text,
  comments text,
  created_at integer,
  updated_at integer
);