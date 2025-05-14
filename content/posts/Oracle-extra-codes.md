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

### Tables & Views

- List all tables,

```sql
select * from all_tables;
```

- List all views,

```sql
select * from all_views;
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

### Triggers

- List all triggers,

```sql
select * from all_triggers;
```

- view the account expiration dates of all users in oracle
- save selected data in another table in oracle

