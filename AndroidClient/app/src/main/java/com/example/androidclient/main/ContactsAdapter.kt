package com.example.androidclient.main

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.androidclient.R
import com.example.androidclient.entity.Person

class ContactsAdapter : RecyclerView.Adapter<ViewHolder>() {
    private val dataList = ArrayList<Person>()

    fun setData(data: List<Person>) {
        dataList.clear()
        dataList.addAll(data)
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        return ViewHolder(
            LayoutInflater.from(parent.context).inflate(
                R.layout.list_item,
                parent,
                false
            )
        )
    }

    override fun getItemCount(): Int = dataList.size

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(dataList[position], isLast = position == dataList.size - 1)
    }

}

class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
    private val textName: TextView = itemView.findViewById(R.id.textName)
    private val textNumber: TextView = itemView.findViewById(R.id.textNumber)

    fun bind(person: Person, isLast: Boolean = false) {
        textName.text = person.name
        textNumber.text = person.phoneNumber

        if (isLast) {
            val lp = itemView.layoutParams as RecyclerView.LayoutParams
            lp.bottomMargin = 16
            itemView.layoutParams = lp
        }
    }

}