export default function PredictionView({ result, onNext }) {
  if (!result) return null;

  // ---------- Confidence Logic (SAFE) ----------
  const losText = result.los || "";
  let risk = "Medium";
  let percent = 50;

  if (losText.includes("5") || losText.includes("6")) {
    risk = "Low";
    percent = 30;
  } else if (losText.includes("12") || losText.includes("14")) {
    risk = "High";
    percent = 75;
  }

  return (
    <div className="card full center">
      <h2 className="title">🧮 Predicted Length of Stay</h2>

      <div className="los-big">{result.los}</div>

      {/* 🔥 CONFIDENCE METER */}
      <div className="confidence-container">
        <div className="confidence-labels">
          <span>Low</span>
          <span>High</span>
        </div>

        <div className="confidence-bar">
          <div
            className={`confidence-fill ${risk.toLowerCase()}`}
            style={{ width: `${percent}%` }}
          />
        </div>

        <p className="confidence-text">
          Risk Level: <strong>{risk}</strong>
        </p>
      </div>

      <button onClick={onNext}>
      <span className="thinking-text">View Clinical Explanation →</span>
       </button>

    </div>
  );
}
