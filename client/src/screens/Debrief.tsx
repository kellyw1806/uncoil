import { useStore } from "@nanostores/react"
import { $plan, $screen } from "../stores/global"

export default function Debrief() {
    const plan = useStore($plan)
    console.log(plan)
    return (
        <div className="w-full h-dvh flex flex-col items-center justify-center">
            <h1 className="font-lusitana-bold text-5xl mb-4">The Plan</h1>
            {plan.exercise_program.map((ex, i) => (
                <p key={i} className="text-xl">{ex.exercise} (15s)</p>
            ))}
            <button 
                onClick={() => $screen.set("feed")} 
                className="mt-4 bg-pinenut70 font-lusitana text-xl py-2 px-8 rounded-lg hover:bg-pinenut transition-colors text-white"
            >
                Start
            </button>
        </div>
    )
}