package com.example.a2_screens.model

import androidx.annotation.DrawableRes
import androidx.annotation.IntegerRes
import androidx.annotation.StringRes

data class Team(
    @IntegerRes val id: Int,
    @StringRes val name: Int,
    @StringRes val abbreviation: Int,
    @DrawableRes val logo: Int
)
