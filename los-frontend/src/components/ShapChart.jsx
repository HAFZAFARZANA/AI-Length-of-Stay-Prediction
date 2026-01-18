import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  Cell,
} from "recharts";

export default function ShapChart({ data }) {
  if (!data || data.length === 0) return null;

  return (
    /* 🔑 FIX: explicit height wrapper */
    <div style={{ width: "100%", height: "320px" }}>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart
          data={data}
          layout="vertical"
          margin={{ top: 10, right: 30, left: 40, bottom: 10 }}
        >
          <XAxis type="number" />
          <YAxis
            type="category"
            dataKey="feature"
            width={140}
          />
          <Tooltip />

          <Bar dataKey="value" radius={[0, 8, 8, 0]}>
            {data.map((_, index) => (
              <Cell
                key={index}
                fill={index === 0 ? "#00ffd5" : "#00c6ff"}
              />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
