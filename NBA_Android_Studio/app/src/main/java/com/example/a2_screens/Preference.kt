package com.example.a2_screens

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.SeekBar
import android.widget.Toast
import androidx.core.content.ContextCompat
import androidx.core.content.ContextCompat.startActivity

class Preference : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_preference)
        val prefArray = resources.getStringArray(R.array.types_of_game)
        val prefMap = prefArray.map { it to 5 }.toMap().toMutableMap()
        val prefButton: Button = findViewById(R.id.back_button)
        val luckyButton: Button = findViewById(R.id.lucky_button)
        prefButton.setOnClickListener{
//            prefButton.addExtraDataToAccessibilityNodeInfo(prefMap)
            go_back(prefButton, prefMap)
        }
        luckyButton.setOnClickListener{
//            prefButton.addExtraDataToAccessibilityNodeInfo(prefMap)
            I_feel_lucky(prefButton, prefMap)
        }


        val seek0: SeekBar = findViewById(R.id.seekBar0)
        seek0.setOnSeekBarChangeListener(object :
            SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seek: SeekBar,
                                           progress: Int, fromUser: Boolean) {
//                prefMap[prefArray[0]] = progress
            }

            override fun onStartTrackingTouch(seek: SeekBar) {
                // write custom code for progress is started
            }

            override fun onStopTrackingTouch(seek: SeekBar) {
                prefMap[prefArray[0]] = seek.progress
                // write custom code for progress is stopped
//                Toast.makeText(this@Preference,
//                    "Progress is: " + seek.progress + "%",
//                    Toast.LENGTH_SHORT).show()
            }
        })

        val seek1: SeekBar = findViewById(R.id.seekBar1)
        seek1.setOnSeekBarChangeListener(object :
            SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seek: SeekBar,
                                           progress: Int, fromUser: Boolean) {
//                prefMap[prefArray[0]] = progress

            }

            override fun onStartTrackingTouch(seek: SeekBar) {

                // write custom code for progress is started
            }

            override fun onStopTrackingTouch(seek: SeekBar) {

                prefMap[prefArray[1]] = seek.progress
            }
        })

        val seek2: SeekBar = findViewById(R.id.seekBar2)
        seek2.setOnSeekBarChangeListener(object :
            SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seek: SeekBar,
                                           progress: Int, fromUser: Boolean) {
//                prefMap[prefArray[0]] = progress

            }

            override fun onStartTrackingTouch(seek: SeekBar) {

                // write custom code for progress is started
            }

            override fun onStopTrackingTouch(seek: SeekBar) {

                prefMap[prefArray[2]] = seek.progress
            }
        })

        val seek3: SeekBar = findViewById(R.id.seekBar3)
        seek3.setOnSeekBarChangeListener(object :
            SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seek: SeekBar,
                                           progress: Int, fromUser: Boolean) {
//                prefMap[prefArray[0]] = progress

            }

            override fun onStartTrackingTouch(seek: SeekBar) {

                // write custom code for progress is started
            }

            override fun onStopTrackingTouch(seek: SeekBar) {

                prefMap[prefArray[3]] = seek.progress
            }
        })
//
//        val seek4: SeekBar = findViewById(R.id.seekBar4)
//        seek4.setOnSeekBarChangeListener(object :
//            SeekBar.OnSeekBarChangeListener {
//            override fun onProgressChanged(seek: SeekBar,
//                                           progress: Int, fromUser: Boolean) {
////                prefMap[prefArray[0]] = progress
//
//            }
//
//            override fun onStartTrackingTouch(seek: SeekBar) {
//
//                // write custom code for progress is started
//            }
//
//            override fun onStopTrackingTouch(seek: SeekBar) {
//
//                prefMap[prefArray[4]] = seek.progress
//            }
//        })


    }
    fun I_feel_lucky(view: View, prefMap: Map<String, Int>) {
        val intent = Intent(this, MainActivity::class.java)
        for ((key, value) in prefMap){
            intent.putExtra(key, 5)
            print(key)
            print(value)
        }


        startActivity(intent)
    }

    fun go_back(view: View, prefMap: Map<String, Int>) {
        val intent = Intent(this, MainActivity::class.java)
        for ((key, value) in prefMap){
            intent.putExtra(key, value)
            print(key)
            print(value)
        }


        startActivity(intent)
    }
}


