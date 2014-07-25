create table posts (
  id integer primary key autoincrement,
  latitude real,
  longitude real,
  title text,
  comment text,
  posted_by text,
  created_at integer
);