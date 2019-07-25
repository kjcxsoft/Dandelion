package com.example.androidclient.common

import android.Manifest

val permissions = listOf(
    Manifest.permission.READ_CONTACTS,
    Manifest.permission.WRITE_CONTACTS
)

const val REQUEST_PERMISSIONS = "request_permission"
const val SHOW_CONTENT = "show_content"

const val SP_NAME = "my_shared_preference"