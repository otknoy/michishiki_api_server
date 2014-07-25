create table posts (
  id integer primary key autoincrement,
  latitude real,
  longitude real,
  posted_by text,
  title text,
  comment text,
  created_at integer
);
