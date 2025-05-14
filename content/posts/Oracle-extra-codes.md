+++
title = "Oracle-extra-codes"
description = "- Show user,"
+++

# Oracle extra codes

## Navigation

### User

- Show user,

```sql
show user;
```

- List all users,

```sql
select * from all_users;
```

- drop user,

```sql
drop user username cascade;
```

### Tables & Views

- List all tables,

```sql
select * from all_tables;
```

- List all views,

```sql
select * from all_views;
```

- Drop table,

```sql
drop table table_name;
```

- description of a table,

```sql
desc table_name;
```

### Profile

- List all profiles,

```sql
select * from dba_profiles;
```

- display a user profile in oracle

```sql
SELECT * FROM dba_profiles
WHERE profile = 'DEFAULT';
```

- view the account expiration dates of all users in oracle

```sql
SELECT username, account_status, expiry_date
FROM dba_users
ORDER BY expiry_date;
```

> just remember the `dba_users` table contains the account expiration dates of all users in Oracle.

- drop profile,

```sql
drop profile profile_name cascade;
```

### Triggers

- List all triggers,

```sql
select * from all_triggers;
```

- Drop trigger,

```sql
drop trigger trigger_name;
```

- disable a trigger in oracle

```sql
alter trigger trigger_name disable;
```

- enable a trigger in oracle

```sql
alter trigger trigger_name enable;
```

