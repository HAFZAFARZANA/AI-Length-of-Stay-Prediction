import { useState } from "react";
import InputForm from "./components/InputForm";
import PredictionView from "./components/PredictionView";
import ExplanationView from "./components/ExplanationView";
import AnimatedBackground from "./components/AnimatedBackground";
import "./App.css";

export default function App() {
  const [step, setStep] = useState(1);
  const [result, setResult] = useState(null);

  return (
    <div className="app-root">
      <AnimatedBackground />

      <div className="page-center">
        {step === 1 && (
          <InputForm
            onSuccess={(data) => {
              setResult(data);
              setStep(2);
            }}
          />
        )}

        {step === 2 && (
          <PredictionView
            result={result}
            onNext={() => setStep(3)}
          />
        )}

        {step === 3 && <ExplanationView result={result} />}
      </div>
    </div>
  );
}
