import { useState } from "react";
import { $exercises, $plan, $screen } from "../stores/global";

export default function Form() {
  const [step, setStep] = useState(0);
  const [formData, setFormData] = useState({
    age: "",
    height: "",
    weight: "",
    injury: "",
    goal: "",
    duration: "15s"
  });
  const [curInput, setCurInput] = useState("");

  const questions = [
    {
      label: "How old are you?",
      name: "age",
      type: "text",
      placeholder: "Enter your age",
    },
    {
      label: "What is your height in cm?",
      name: "height",
      type: "text",
      placeholder: "Enter your height (cm)",
    },
    {
      label: "What is your weight in kg?",
      name: "weight",
      type: "text",
      placeholder: "Enter your weight (kg)",
    },
    {
      label: "What body part would you like to focus on?",
      name: "injury",
      type: "text",
      placeholder: "Enter your answer",
    },
    {
      label: "What are you working to improve? e.g. strength, flexibility, rehab, etc.",
      name: "goal",
      type: "text",
      placeholder: "Enter your answer",
    },
  ];

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setCurInput(e.target.value);
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const nextStep = async () => {
    setCurInput("");
    if (step < questions.length - 1) {
      setStep(step + 1);
    } else {
      try {
        console.log("Sending plan")
        const response = await fetch('http://localhost:8000/plan', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(formData)
        })
        if (!response.ok) throw new Error('Network response was not ok')
  
        const result = await response.json()
        $exercises.set(result.exercises)
        $plan.set(JSON.parse(result.plan))
        $screen.set("debrief")
        console.log(result)
  
      } catch (error) {
        console.error('There was a problem with the fetch operation:', error)
      }
      console.log("Form submitted:", formData);
    }
  };

  const prevStep = () => {
    setCurInput("");
    if (step > 0) setStep(step - 1);
  };

  return (
    <div className="h-screen w-full bg-sawdust flex">
      <div className="w-full bg-pinenut flex h-32 mt-16 w-full items-center">
        <div className="flex ml-16 mt-2">
          <h1 className="text-7xl text-left font-lusitana text-sawdust">uncoil</h1>
        </div>
      </div>
      <div className="font-inknut absolute text-darkoak text-center" style={{"top": "38%", "right": "11.5%", "fontSize": "2rem"}}>
        help us get to know you better
      </div>
      <div className="w-full max-w-xl p-8 shadow-lg rounded-lg h-96 absolute bg-pinenut border-darkoak border-8" style={{"top": "35%", "right": "10%"}}>

        <div className="transition-all py-8 px-4 justify-center items-center flex flex-col mt-auto">
          <h2 className="text-3xl mb-4 font-inknut text-sawdust text-center">
            {questions[step].label}
          </h2> 
            <input
              type={questions[step].type}
              name={questions[step].name}
              value={curInput}
              onChange={handleChange}
              placeholder={questions[step].placeholder}
              className="w-full p-4 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
            />
          
        </div>

        <div className="flex justify-between">
          {step > 0 && (
            <button
              onClick={prevStep}
              className="bg-gray-300 px-4 py-2 rounded-lg hover:bg-gray-400"
            >
              Back
            </button>
          )}
          <button
            onClick={nextStep}
            className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600"
          >
            {step < questions.length - 1 ? "Next" : "Submit"}
          </button>
        </div>
      </div>
    </div>
  );
}
