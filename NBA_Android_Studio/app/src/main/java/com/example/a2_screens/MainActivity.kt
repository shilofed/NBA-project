package com.example.a2_screens

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.*
import android.widget.AdapterView.OnItemClickListener

import android.widget.AutoCompleteTextView




class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val preferences = resources.getStringArray(R.array.types_of_game)
//        val arrayAdapter = ArrayAdapter(this, R.layout.dropdown_item, preferences)
        var arg = ""
        for (pref in resources.getStringArray(R.array.types_of_game)){
            val curPref=intent.getIntExtra(pref, 5)
            arg = "$arg$pref=$curPref;"
        }

        val rollButton: Button = findViewById(R.id.button)
        rollButton.setOnClickListener{
            switchToGameRecScreen(rollButton, arg)
        }
        val prefButton: Button = findViewById(R.id.pref_button)
        prefButton.setOnClickListener{
            switchToPrefScreen(prefButton)
        }
        val futureButton: Button = findViewById(R.id.future_button)
        futureButton.setOnClickListener{
            getPredictFutureGame(futureButton, arg)
        }
    }

    fun switchToGameRecScreen(view: View, preference : String){
        val intent = Intent(this, DisplayMassageActivity::class.java)
        intent.putExtra("preference", preference)
        intent.putExtra("predict", false)
        startActivity(intent)
    }

    fun getPredictFutureGame(view: View, preference : String){
        val intent = Intent(this, DisplayMassageActivity::class.java)
        intent.putExtra("preference", preference)
        intent.putExtra("predict", true)
        startActivity(intent)
    }

    fun switchToPrefScreen(view: View){
        val intent = Intent(this@MainActivity, Preference::class.java)
//        intent.putExtra("preference", preference)
        startActivity(intent)
    }

}