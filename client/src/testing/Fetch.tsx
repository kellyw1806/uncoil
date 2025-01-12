import { Button, Input } from "antd"
import { useState } from "react"

export default function Fetch() {
  const [exercises, setExercises] = useState([])
  const [age, setAge] = useState(25)

  const handleClick = async () => {
    const data = {
      age: age,
      weight: 70,
      height: 175
    }

    try {
      const response = await fetch('http://localhost:8000/plan', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
      if (!response.ok) throw new Error('Network response was not ok')

      const result = await response.json()
      setExercises(result.exercises)

    } catch (error) {
      console.error('There was a problem with the fetch operation:', error)
    }
  }

  return (
    <div>
      <Input
        type="number"
        value={age}
        onChange={(e) => setAge(parseInt(e.target.value))}
        placeholder="Enter age"
        className="w-auto"
      />
      <Button onClick={handleClick}>
        Test Function 1
      </Button>
      <ul>
        {exercises.map((exercise, index) => (
          <li key={index}>{exercise}</li>
        ))}
      </ul>
    </div>
  )
}