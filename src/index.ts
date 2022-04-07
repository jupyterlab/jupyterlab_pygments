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
    console.log('JupyterLab extension jupyterlab_pygments is activated!');
  }
};

export default plugin;
