import { useState } from "react";

const RANGES = {
  rcount: [0, 10],
  respiration: [12, 30],
  pulse: [50, 140],
  bmi: [15, 45],
  creatinine: [0.5, 3.5],
  neutrophils: [30, 80],
};

export default function InputForm({ onSuccess }) {
  const [form, setForm] = useState({
    rcount: "",
    gender: "M",
    respiration: "",
    pulse: "",
    bmi: "",
    creatinine: "",
    neutrophils: "",
  });

  const [errors, setErrors] = useState({});

  // 🔑 Validate single field
  const validate = (name, value) => {
    if (!RANGES[name]) return "";

    const [min, max] = RANGES[name];
    if (value === "") return "Required";
    if (value < min || value > max)
      return `Value must be between ${min} and ${max}`;

    return "";
  };

  // 🔄 Handle input change
  const handleChange = (e) => {
    const { name, value } = e.target;

    const error = validate(name, value);

    setForm({ ...form, [name]: value });
    setErrors({ ...errors, [name]: error });
  };

  // 🚫 Prevent submit if errors exist
  const hasErrors =
    Object.values(errors).some((e) => e) ||
    Object.keys(RANGES).some((k) => form[k] === "");

  const submit = async () => {
    if (hasErrors) return;

    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        rcount: +form.rcount,
        gender: form.gender,
        respiration: +form.respiration,
        pulse: +form.pulse,
        bmi: +form.bmi,
        creatinine: +form.creatinine,
        neutrophils: +form.neutrophils,
      }),
    });

    const data = await res.json();
    onSuccess(data);
  };

  return (
    <div className="card full">
      <h1>🏥 Patient LOS Prediction</h1>
      <p className="subtitle">AI-based Hospital Stay Estimation</p>

      <div className="form-grid">
        {Object.entries(RANGES).map(([key, [min, max]]) => (
          <Field
            key={key}
            label={`${key.toUpperCase()} (${min}–${max})`}
            name={key}
            value={form[key]}
            error={errors[key]}
            onChange={handleChange}
          />
        ))}

        <div className="field">
          <label>Gender</label>
          <select
            name="gender"
            value={form.gender}
            onChange={handleChange}
          >
            <option value="M">Male</option>
            <option value="F">Female</option>
          </select>
        </div>
      </div>

      <button disabled={hasErrors} onClick={submit}>
        Predict LOS
      </button>
    </div>
  );
}

function Field({ label, name, value, onChange, error }) {
  return (
    <div className="field">
      <label>{label}</label>
      <input
        name={name}
        value={value}
        onChange={onChange}
        type="number"
        className={error ? "invalid" : ""}
      />
      {error && <span className="error">{error}</span>}
    </div>
  );
}
