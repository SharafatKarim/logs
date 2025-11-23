+++
title = "Checksum-of-a-google-drive-file"
description = "A checksum (hash) lets you verify a file has not been altered or corrupted. Common use: confirm a downloaded ISO matches the publisher’s SHA-256 hash."
+++

# Checksum of a Google Drive File

A checksum (hash) lets you verify a file has not been altered or corrupted. Common use: confirm a downloaded ISO matches the publisher’s SHA-256 hash.

## 1. Open Google Colab

Go to <https://colab.research.google.com> and create a new Python notebook.

## 2. Connect to Google Drive

Run:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Approve the auth prompt. Your Drive files appear under `/content/drive/MyDrive/`.

## 3. Locate the File Path

In the left sidebar (folder icon):

- Navigate to the file.
- Right‑click the file and choose "Copy path" (or manually note its path).
Example path: `/content/drive/MyDrive/DATA/iso/Win11_24H2_English_x64_Custom_Optimized.iso`

## 4. Compute the SHA‑256 Checksum

Use `sha256sum` (installed by default in Colab):

```python
!sha256sum /content/drive/MyDrive/DATA/iso/Win11_24H2_English_x64_Custom_Optimized.iso
```

Output format:

```shell
<sha256_hash>  <file_path>
```

## 5. Verify Against Known Hash

Compare the printed hash with the official one from the source website. They must match exactly. If not, the file may be incomplete or tampered with.

## Common Issues

- File not found: Confirm the path (case sensitive).
- Large files: Hashing can take time; wait for completion.
- Different algorithm needed: Replace with `!md5sum` or `!sha1sum` (only if required; SHA‑256 is stronger).

