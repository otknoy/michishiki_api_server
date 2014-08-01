create table posts (
  id integer primary key autoincrement,
  title text,
  comment text,
  posted_by text,
  rate integer,
  latitude real,
  longitude real,
  created_at integer,
  updated_at integer
);