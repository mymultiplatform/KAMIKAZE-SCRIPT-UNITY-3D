using UnityEngine;
using UnityEngine.Rendering;

public class KamikazeEnvironmentReset : MonoBehaviour
{
    void Start()
    {
        OverwriteWorld();
        Debug.Log("☢ ENVIRONMENT HARD RESET COMPLETE");
    }

    void OverwriteWorld()
    {
        // ===== AMBIENT LIGHTING =====
        RenderSettings.ambientMode = AmbientMode.Skybox;
        RenderSettings.ambientIntensity = 1f;

        RenderSettings.ambientLight = Color.white;
        RenderSettings.ambientSkyColor = Color.white;
        RenderSettings.ambientEquatorColor = new Color(0.54f, 0.54f, 0.54f);
        RenderSettings.ambientGroundColor = new Color(0.25f, 0.25f, 0.25f);

        // ===== FOG =====
        RenderSettings.fog = false;
        RenderSettings.fogMode = FogMode.Exponential;
        RenderSettings.fogColor = Color.gray;
        RenderSettings.fogDensity = 0.01f;

        // ===== SKYBOX =====
        if (RenderSettings.skybox != null)
        {
            if (RenderSettings.skybox.HasProperty("_Exposure"))
                RenderSettings.skybox.SetFloat("_Exposure", 1f);

            if (RenderSettings.skybox.HasProperty("_Tint"))
                RenderSettings.skybox.SetColor("_Tint", Color.white);
        }

        // ===== LIGHTS =====
        Light[] lights = FindObjectsOfType<Light>();

        if (lights.Length == 0)
        {
            GameObject sun = new GameObject("Directional Light");
            Light l = sun.AddComponent<Light>();
            l.type = LightType.Directional;
            l.color = Color.white;
            l.intensity = 1f;
            sun.transform.rotation = Quaternion.Euler(50f, -30f, 0f);
        }
        else
        {
            foreach (Light l in lights)
            {
                if (l.type == LightType.Directional)
                {
                    l.color = Color.white;
                    l.intensity = 1f;
                    l.transform.rotation = Quaternion.Euler(50f, -30f, 0f);
                }
            }
        }

        // ===== FORCE UNITY TO SAVE LIGHTING INTO SCENE =====
#if UNITY_EDITOR
        UnityEditor.SceneManagement.EditorSceneManager.MarkSceneDirty(
            UnityEngine.SceneManagement.SceneManager.GetActiveScene()
        );
#endif
    }
}
