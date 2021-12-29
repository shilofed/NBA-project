package com.example.a2_screens

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        var rollButton: Button = findViewById(R.id.button)
//        rollButton.setOnClickListener{
//            Context context =
//        }
    }
    fun switch_screen(view: View){
//        val intent = Intent()
//        startActivity(intent)
//        DisplayMassageActivity()
        val intent = Intent(this, DisplayMassageActivity::class.java)
        startActivity(intent)
//        val resultTextView: TextView = findViewById(R.id.textView)
//        resultTextView.text = 7.toString()
    }
}