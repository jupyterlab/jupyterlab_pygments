import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

/**
 * Initialization data for the jupyterlab_pygments extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jupyterlab_pygments:plugin',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    // This plugin only brings CSS style rules
  }
};

export default plugin;
